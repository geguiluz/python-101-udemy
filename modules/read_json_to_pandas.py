import pandas as pd
import files.file_handler as fh

# Reading JSON data from a file
json_data = fh.open_json_file("data.json", "input")

print(json_data)
# Converting JSON data to a pandas DataFrame
"""
# Deprecated pd.read_json(json_data) Literal json strings are no longer valid.
# Provide full path instead:
df = pd.read_json(
    "/Users/memo/code-projects/self-learning/learning-python/python-101-udemy/input/data.json"
)
"""
"""
# Didn't quite like the following result as json is not normalized
df = pd.json_normalize(json_data["orderLogisticalInformation"])
print(df)
"""
# Other option that might be useful:
df = pd.json_normalize(json_data)
df.to_csv(
    "/Users/memo/code-projects/self-learning/learning-python/python-101-udemy/output/data_pandas.csv"
)
