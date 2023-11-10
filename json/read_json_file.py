import json

with open('output/user.json') as jf:
    # load() converts a jason file to a dictionary
    user = json.load(jf)

print(type(user))
print(user)

fav_nums = user['fav_nums']
print(type(fav_nums))
print(fav_nums)
