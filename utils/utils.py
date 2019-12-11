import json


def write_file(data, path):
    with open(path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def print_json(data):
    json = json.dumps(data, sort_keys=True,
                      indent=4, ensure_ascii=False)
    print(json)
