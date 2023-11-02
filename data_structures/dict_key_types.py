# Values in dictionaries must be hashable. Any mix works

# Creating a dictionary with a key that is unhashable (i.e. lists)
# TypeError: unhashable type: 'list'
# sample = {[1, 2]: "Test"}

# This is useful if we want to have a conversion of values between different types
sample = {
    True: "Yes",
    False: "No",
    1: "One",
    "One": 1,
}
print(sample)
