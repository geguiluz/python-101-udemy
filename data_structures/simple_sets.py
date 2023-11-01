names = {"Greg", "Brooke", "Mark", "Daisy"}

print(names)

names.add("Kath")
print(f"After add: {names}")

# Remove a person
names.remove("Mark")
print(f"After remove: {names}")

# Clear set
# Python prints set() so that it's not confused for a dictionary
names.clear()
print(f"After clear: {names}")
