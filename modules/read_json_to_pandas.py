# import pandas as pd
import json
import files.file_handler as fh

# Reading JSON data from a file
f = fh.open_file("data.json", "input")
json_data = json.load(f)
print(json_data)

# Converting JSON data to a pandas DataFrame
# df = pd.read_json(json_data)
