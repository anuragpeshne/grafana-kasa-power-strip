import json
import re

subregex = re.compile(r"(\d):")
def parse_powerdb_line(line):
    timestamp, json_str = line.split(',', 1)

    timestamp = int(timestamp) * 1000 # millisecond timestamp
    double_quoted_json_str = json_str.strip("'<>() ").replace('\'', '\"')
    valid_index_name_json_str = subregex.sub(r'"\1":', double_quoted_json_str)
    if (len(valid_index_name_json_str) == 0):
        return (timestamp, "")

    try:
        parsed_json = json.loads(valid_index_name_json_str)
    except Exception as e:
        print(line)
        print(e)
        parsed_json = ""
    return (timestamp, parsed_json)

class PowerDbReader:
    def __init__(self, db_file_path):
        self.total_plugs = 6
        self.db = self.parse(db_file_path)

    def parse(self, db_file_path):
        parsed_data = []
        with open(db_file_path, 'r') as db_file:
            lines = [line.strip() for line in db_file]
            for line in lines:
                timestamp, reading = parse_powerdb_line(line)
                if (len(reading) > 0):
                    parsed_data.append((timestamp, reading))
        print("parsed lines" + str(len(parsed_data)))
        return parsed_data

    def get_plug_names(self):
        return ['Plug ' + str(i + 1) for i in range(self.total_plugs)]

    def plug_name_to_id(self, name):
        return str(int(name[-1]) - 1)

    def get_data_in_range(self, target_plug, from_, to):
        target_plug = str(target_plug)
        i = 0
        in_range_data = []
        while i < len(self.db) and self.db[i][0] < from_:
            i += 1
        while i < len(self.db) and self.db[i][0] < to:
            in_range_data.append(
                [
                    self.db[i][1][target_plug]['power_mw'],
                    self.db[i][0]
                ]
            )
            i += 1

        return in_range_data
