from pymongo import MongoClient
from util.json_util import load_json_file

vm_ip = "172.31.253.69"
local_ip = "0.0.0.0"


def insert_data(data: list, collection_name="poi_info", ip=vm_ip, port=27017):
    # Create connection to MongoDB
    client = MongoClient(ip, port, username='root', password='1234567890')
    db = client['poi']
    col = db[collection_name]

    x = col.insert_many(data)
    # print list of the _id values of the inserted documents:
    print(x.inserted_ids)


if __name__ == '__main__':
    data = load_json_file.load_file("../../data/poi/poi_elem.json")
    output = []
    from util.coordinates import transformation
    for key in data:
        record = data[key]
        lat = float(record["LAT"])
        lng = float(record["LNG"])
        record["LNG"], record["LAT"] = transformation.wgs84_to_gcj02(lng, lat)
        output.append(record)

    insert_data(output, collection_name="poi_500m", ip=vm_ip)
