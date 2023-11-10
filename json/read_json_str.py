import json

car_str = '{"make": "Tesla", "Model": "Model Y"}'

# json.loads() converts json string to dictionary
car = json.loads(car_str)

print(type(car))
print(car)

num_str = '[1, 2, 3]'
nums = json.loads(num_str)

print(type(nums))
print(nums)
