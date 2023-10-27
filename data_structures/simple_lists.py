names = ["Mark", "Daisy", "Brian"]

# Print all names in list
print(names)

# Print a specific index of list
print(names[2])

# Update name by index
names[1] = "Martha"

# Print all names in list
print(names)

# Append name
names.append("Greta")

# Print all names in list
print(names)

# Extend names with 3 more items
names.extend(["Celia", "Robert", "Max"])

# Print all names in list
print(names)

# Remove item
# If not in list, system returns ValueError: list.remove(x): x not in list
names.remove("Robert")

# Print all names in list
print(names)

# Remove name from list by index using pop
names.pop(3)

# Print all names in list
print(names)
