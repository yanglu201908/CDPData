import json


def load_file(file_path="data/poi/poi_all.json"):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    path = "../../data/poi/poi_all.json"
    print(load_file(path)["0ff88c16-25b6-418d-8935-6ee320fcdd9d"])
