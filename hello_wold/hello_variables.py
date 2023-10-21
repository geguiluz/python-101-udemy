name = "Mark"
age = 35
is_required = False

print(name)
print(age)
print(is_required)

# This is a newer way of formatting, but not ideal
print("Your name is {} and your age is {}".format(name, age))

# There is a newer way of formatting strings
message = f'Your name is {name} and your age is {age}'
print(message)
