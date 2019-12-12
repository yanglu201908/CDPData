from util.json_util import load_json_file
from util.mongo import crud


def save_to_mongo():
    data = load_json_file.load_file(
        file_path="/Users/yanglu/Desktop/wework/CDPData/data/cdpData/buildingInfo/buildingInfoProcessed.json")
    output = []

    for key in data:
        record = data[key]
        output.append(record)

    crud.insert_data(output, collection_name="buildingInfo")


if __name__ == '__main__':
    save_to_mongo()
