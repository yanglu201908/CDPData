import json


def dump_json_to_file(file:dict, path="poi_all.json"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)
