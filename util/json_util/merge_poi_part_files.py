import json
from util.json_util import save_2_file
from util import walk_dir, merge_dict


def merge_all_poi_file(base_path, ext, output_path):

    file_lists = walk_dir.file_list(base_path, ext)
    poi_data = {}
    for file in file_lists:
        with open(file) as f:
            data_tmp = json.load(f)
        poi_data = merge_dict.merge_dict(data_tmp, poi_data)
    save_2_file.dump_json_to_file(poi_data, path=output_path)


if __name__ == '__main__':
    base_path = "../../data/output"
    ext = ".cdpData"
    output_path = "../../data/poi/poi_all.cdpData"
    merge_all_poi_file(base_path=base_path, ext=ext, output_path=output_path)
