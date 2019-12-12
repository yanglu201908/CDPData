from util.load_csv import load_csv
from dataProcessing.buildingInfo.industryType import industry
from util.json_util import save_2_file
from util.coordinates import transformation
import json


def load_building_data(path="../../data/cdpData/buildingInfo/buildingInfo.csv"):
    return load_csv.load_data(path)


def main():

    buildingInfo = {}
    buildingDataRaw = load_building_data()
    building_uuid = buildingDataRaw.BUILDINGUUID.to_list()

    df = buildingDataRaw.set_index('BUILDINGUUID')

    amenitiesList = []

    for uuid in building_uuid:

        infoFromRaw = df.loc[uuid]

        buildingInfo[uuid] = {}
        buildingInfo[uuid]["uuid"] = uuid
        buildingInfo[uuid]["name"] = infoFromRaw.BUILDINGNAMEENG
        buildingInfo[uuid]["nameChinese"] = infoFromRaw.BUILDINGNAMECHN
        buildingInfo[uuid]["city"] = infoFromRaw.BUILDINGCITY.lower()
        lat = float(infoFromRaw.LATITUDE)
        lng = float(infoFromRaw.LONGITUDE)
        buildingInfo[uuid]["lng"], buildingInfo[uuid]["lat"] = transformation.wgs84_to_gcj02(lng, lat)
        buildingInfo[uuid]["address"] = infoFromRaw.ADDRESSCHN
        buildingInfo[uuid]["districtName"] = infoFromRaw.DISTRICTNAME
        buildingInfo[uuid]["buildingOpenDate"] = infoFromRaw.BUILDINGOPENDATE

        # special amenities
        buildingInfo[uuid]["specialAmenities"] = ['"yoga", "babyRoom"']

        # gender distribution
        buildingInfo[uuid]["genderDistribution"] = {}

        buildingInfo[uuid]["genderDistribution"]["malePCT"] = "50%"
        buildingInfo[uuid]["genderDistribution"]["femalePCT"] = "50%"

        # industry distribution
        industry_list = industry.keys()

        fakePCT = 100/len(industry_list)

        buildingInfo[uuid]["industryDistribution"] = {}

        for ind in industry_list:
            buildingInfo[uuid]["industryDistribution"][ind] = str(int(fakePCT)) + "%"

        # amenities
        ams = "".join(infoFromRaw.AMENITIES)
        am_list = json.loads(ams)

        for am in am_list:

            amenity = am["name"]

            if amenity not in amenitiesList:

                amenitiesList.append(amenity)

            else:

                pass

    for uuid in building_uuid:

        infoFromRaw = df.loc[uuid]

        buildingInfo[uuid]["amenities"] = {}

        for am in amenitiesList:
            buildingInfo[uuid]["amenities"][am] = "0"

        ams = "".join(infoFromRaw.AMENITIES)
        am_list = json.loads(ams)

        for dictionary in am_list:

            amenity = dictionary["name"]
            buildingInfo[uuid]["amenities"][amenity] = "1"


    save_2_file.dump_json_to_file(file=buildingInfo, path="../../data/cdpData/buildingInfo/buildingInfoProcessed.json")


if __name__ == '__main__':
    print(main())
