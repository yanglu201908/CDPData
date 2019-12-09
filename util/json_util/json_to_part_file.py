import codecs
import json
import os


def to_json(data, base_path="data/output/", location_finished_crawling_count=0, ensure_ascii=False):
    """
            Args:
                data: json data to be store to local file.
                base_path: is the directory of output files folder.
                location_finished_crawling_count: indicating which building's POI info in storing into local file

    """

    file_type = ".json"
    path = os.path.join(base_path, "part_" + str(location_finished_crawling_count)+file_type)

    wfobj = codecs.open(path, 'w', encoding="utf-8")
    json.dump(data, wfobj, indent=4, ensure_ascii=ensure_ascii)
    wfobj.close()


if __name__ == '__main__':
    print(os.path.join("data/output/", "part_" + str(0) + ".json"))
