import json
import os
from elasticsearch import Elasticsearch
from vs import v1

class ESConnector:
    def __init__(self):
        self.es = Elasticsearch()

    def init(self, index_name: str):
        """
        Gather a Counter object of tokens in the file and their count.
        :param file: the path to the file.
        :param lang: the language of file.
        :return: a Counter object of items: token and count.
        """
        dir_path = os.path.dirname(__file__)
        index_schema_path = f"{dir_path}/index_schemas/{index_name}.json"

        try:
            with open(index_schema_path, "r", encoding='utf-8') as schema:
                res = self.es.indices.create(index=index_name,
                                             ignore=400,
                                             body=json.loads(schema.read()))
            return res
        except IOError as e:
            return {'status': 'error', 'errors': e}

   
if __name__ == '__main__':
    pass
