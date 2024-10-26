import json

json_file_path = './files/red_data.json'


def read_reds():
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for a in data:
            if a["ac"] == 10:
                print(a["ac"], "--", a["red"])


read_reds()
