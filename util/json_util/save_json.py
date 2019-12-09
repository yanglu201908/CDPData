import codecs
import json
import os


def to_json(data, filename:str, base_path="data/output/", ensure_ascii=False):
    """
            Args:
                data: json data to be store to local file.
                filename: file name for this json file
                base_path: is the directory of output files folder.
                ensure_ascii: this will ascii coding
    """

    file_type = ".json"
    path = os.path.join(base_path, str(filename)+file_type)

    wfobj = codecs.open(path, 'w', encoding="utf-8")
    json.dump(data, wfobj, indent=4, ensure_ascii=ensure_ascii)
    wfobj.close()
