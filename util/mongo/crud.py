from pymongo import MongoClient
from util.json_util import load_json_file

vm_ip = "172.31.253.69"
local_ip = "0.0.0.0"


def insert_data(data: dict, collection_name="poi_info", ip="0.0.0.0", port=27017):
    # Create connection to MongoDB
    client = MongoClient(ip, port, username='root', password='1234567890')
    db = client['poi']
    collection = db[collection_name]

    # Build an example dictionary
    # d = {'website': 'www.BAIDU.com', 'haha': 'lol', 'colour': 'blue'}

    # Insert the dictionary into Mongo
    collection.insert(data)


if __name__ == '__main__':
    data = load_json_file.load_file("../../data/poi/poi_all.json")
    uuids = data.keys()
    for uuid in uuids:
        building_poi_info = data[uuid]
        building_poi_info["building_location_uuid"] = uuid
        insert_data(building_poi_info, ip=vm_ip)
