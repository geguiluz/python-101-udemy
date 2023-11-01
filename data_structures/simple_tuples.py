things = ("Car", "Fan", "Cup", "Mug", "Glass", "Mug")

print(things)

# Number of times 'Mug' appears
mug_count = things.count("Mug")
print(f"Mug appears {mug_count} times.")

# Index of "Mug"
mug_index = things.index("Mug")
print(f"Index of Mug is: {mug_index}.")

# Get items by index
first_item = things[0]
print(f"First item: {first_item}.")

# TypeError: 'tuple' object does not support item assignment
# things[0] = "New thing"
