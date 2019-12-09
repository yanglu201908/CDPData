import json


def dump_json_to_file(file: dict, path="data/competitor_poi_all.cdpData"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)
