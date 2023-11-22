# import pandas as pd
import json
from modules.files import file_handler as fh

# Reading JSON data from a file
with open("data.json") as f:
    json_data = json.load(f)

# Converting JSON data to a pandas DataFrame
# df = pd.read_json(json_data)
