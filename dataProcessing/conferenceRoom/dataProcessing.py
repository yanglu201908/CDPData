from util.load_csv import load_csv
from util.json_util import save_2_file


def load_data(path="../../data/cdpData/conferenceRoom/confRoom.csv"):
    return load_csv.load_data(path)


def process(path="../../data/cdpData/conferenceRoom/confRoom.csv"):

    confRoomInfo = {}

    raw_df = load_data(path)
    conf_room_uuid_list = raw_df.CONFERENCEROOMUUID.to_list()

    df_with_index = raw_df.set_index('CONFERENCEROOMUUID')

    for conf_room_uuid in conf_room_uuid_list:

        if conf_room_uuid not in confRoomInfo:

            confRoomInfo[conf_room_uuid] = {}

        info = df_with_index.loc[conf_room_uuid]

        confRoomInfo[conf_room_uuid]["buildingUUID"] = str(info.BUILDINGUUID)
        confRoomInfo[conf_room_uuid]["conferenceRoomName"] = str(info.CONFERENCEROOMNAME)
        confRoomInfo[conf_room_uuid]["conferenceRoomCapacity"] = str(info.CONFERENCEROOMCAPACITY)
        confRoomInfo[conf_room_uuid]["weeklyBookedHours"] = str(info.WEEKLYBOOKEDHOURS)

    save_2_file.dump_json_to_file(file=confRoomInfo, path="../../data/cdpData/conferenceRoomInfo/conferenceRoomInfoProcessed.json")


if __name__ == '__main__':
    process()
