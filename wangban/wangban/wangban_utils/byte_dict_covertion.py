import json

def byte_to_dict(item):
    try:
        links_dict = json.loads(item.decode('utf-8').replace("'", "\""))
    except Exception as e:
        print('byte_to_dict error',e)
        return False
    return links_dict

def dict_to_byte(links_dict):
    try:
        links_dict = json.dumps(links_dict)
    except Exception as e:
        print('dict_to_byte error',e)
        return False
    return links_dict