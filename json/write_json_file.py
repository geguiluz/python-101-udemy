import os
import json

dir_path =  os.path.join(os.getcwd(), 'output')
os.makedirs(dir_path, exist_ok=True)
json_path = os.path.join(dir_path, 'user.json')

user = {
    'name':'Mike',
    'age': 56,
    'is_active': [1, 6, 3, 8, 4],
}

with open(json_path, 'w') as jf:
    # json.dump() can be used with minimal arguments as follows:
    # json.dump(user, jf)
    """ 
    json.dump() has additional optional arguments:
    sort_keys - Sorts keys in alphabetical order
    indent - Similar to beautify
    """
    json.dump(user, jf, sort_keys=True, indent=4)
