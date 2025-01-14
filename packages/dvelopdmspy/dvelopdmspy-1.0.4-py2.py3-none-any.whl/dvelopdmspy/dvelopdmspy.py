import json
import logging
import os

import humps
from dvelopdmspy.rest_adapter import RestAdapter
from dvelopdmspy.exceptions import DvelopDMSPyException
from dvelopdmspy.models import *


def sanitize_doc(doc_dict) -> DmsDocument:
    doc = dict(humps.decamelize(doc_dict))
    doc["id_"] = doc.pop("id")
    doc["links"] = doc.pop("_links")
    t_doc = DmsDocument(**doc)
    return t_doc


class DvelopDmsPy:
    def __init__(self, hostname: str, api_key: str, repository: str = None,
                 logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_key, repository, logger)
        self._source_mappings = self.get_mappings()

    def get_mappings(self) -> Mappings:
        t_result = self._rest_adapter.get(endpoint='source')
        t_result.data = dict(humps.decamelize(t_result.data))
        t_result.data["id_"] = t_result.data.pop("id")
        return Mappings(**t_result.data)

    def _get_property_key_from_name(self, property_name: str) -> str:
        for prop in self._source_mappings.properties:
            if prop.display_name.lower() == property_name.lower():
                return str(prop.key)

    def _get_category_key_from_name(self, category_name: str) -> str:
        for cat in self._source_mappings.categories:
            if cat.display_name.lower() == category_name.lower():
                return str(cat.key)

    def add_property(self, display_name: str, pvalue, pdict: dict = None) -> dict:
        if pdict is None:
            pdict = {}
        t_key = self._get_property_key_from_name(display_name)
        if type(pvalue) != list:
            pvalue = [pvalue]
        pdict[t_key] = pvalue
        return pdict

    def add_upload_property(self, display_name: str, pvalue, plist: list = None) -> list:
        if plist is None:
            plist = []
        t_key = self._get_property_key_from_name(display_name)
        if type(pvalue) != list:
            pvalue = [pvalue]
        plist.append({
            'key': t_key,
            'values': pvalue
        })
        return plist

    def add_category(self, display_name, plist: list = None) -> list:
        if plist is None:
            plist = []
        t_key = self._get_category_key_from_name(display_name)
        plist.append(t_key)
        return plist

    def archive_file(self,
                     filepath: str,
                     category_id: str,
                     properties: list[dict]) -> str | bool:
        # Blob Upload
        blob_endpoint = "blob/chunk/"
        result = self._rest_adapter.post(endpoint=blob_endpoint, binary_upload=True, upload_file_path=filepath)
        if result.status_code != 201 or "location" not in result.headers:
            raise DvelopDMSPyException("BLOB upload failed. No blob location detected")
        blob_location = result.headers["location"]

        # Archivdokument erstellen und mit Blob verbinden
        blob_to_doc_endpoint = "o2m"

        release_property = {
            'key': 'property_state',
            'values': [
                'Release'
            ]
        }
        properties.append(release_property)

        post_body = {
            'filename': os.path.basename(filepath),
            'sourceCategory': category_id,
            'sourceId': f'/dms/r/{self._rest_adapter.repository}/source',
            'contentLocationUri': blob_location,
            'sourceProperties': {
                'properties': properties
            }
        }

        result = self._rest_adapter.post(endpoint=blob_to_doc_endpoint, data=post_body)
        try:
            t_loc = result.headers.get("Location")
            t_doc_id = t_loc.split('?')[0].split('/')[-1]
        except (KeyError, ValueError):
            t_doc_id = "unknown"

        return t_doc_id

    def get_documents(self,
                      properties: dict[SearchProperty] = None,
                      categories: list[str] = None,
                      limit: int = None,
                      doc_id: str = None) -> List[DmsDocument]:
        ret_docs = []
        params = {
            "sourceid": f"/dms/r/{self._rest_adapter.repository}/source"
        }
        if properties is not None:
            params["sourceproperties"] = json.dumps(properties)
        print(params.get("sourceproperties"))

        if categories is not None:
            params["sourcecategories"] = json.dumps(categories)
        print(params.get("sourcecategories"))

        # Wurde eine doc_id angegeben, brauchen wir keinen Recherche
        if doc_id is not None:
            endpoint = f"o2m/{doc_id}"
        else:
            endpoint = "srm"

        result = self._rest_adapter.get(endpoint=endpoint, ep_params=params, limit=limit)
        if type(result.data) == list:
            for doc in result.data:
                t_doc = sanitize_doc(doc)
                ret_docs.append(t_doc)
        else:
            t_doc = sanitize_doc(result.data)
            ret_docs.append(t_doc)

        return ret_docs

    def key_to_display_name(self, key) -> str:
        if type(key) == list:
            for tk in key:
                if len(tk) > 10:
                    key = tk
                    break
        for prop in self._source_mappings.properties:
            if str(prop.key) == key:
                return prop.display_name

        for cat in self._source_mappings.categories:
            if str(cat.key) == key:
                return cat.display_name

        return ""

    def download_doc_blob(self, doc_id: str, dest_file: str, dl_href: str = None) -> bool:
        # Wurde die Funktion aus einem Dokument heraus aufgerufen, kennen wir den Pfad zum Blob bereits
        if dl_href is None:
            t_docs = self.get_documents(doc_id=doc_id)
            if len(t_docs) == 0:
                raise DvelopDMSPyException("Document not found.")
            t_doc = t_docs[0]
            dl_href = t_doc.links.mainblobcontent

        host_base = f"https://{self._rest_adapter.host_base}"
        result = self._rest_adapter.get(endpoint=dl_href, base_url=host_base, binary=True)

        with open(dest_file, 'wb') as out_file:
            out_file.write(result.raw.content)

        return True

    def get_property_value(self, doc_obj: DmsDocument, prop_display_name: str):
        prop_key = self._get_property_key_from_name(prop_display_name)
        for prop in doc_obj.source_properties:
            if prop.key == prop_key:
                if prop.values is None:
                    return prop.value
                else:
                    return prop.values
