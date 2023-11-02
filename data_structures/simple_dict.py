dog = {"name": "Daisy", "Breed": "Chihuahua", "Colour": "Fawn"}

print(dog)

dog["age"] = 10
print(dog)

dog["age"] = 11
print(dog)

age = dog.pop("age")
print(f"Removed: {age}")
print(dog)

# Returns the default of 'None' if default value not set
# Age after removing it: None
# Age after removing it: Age not set
age = dog.get("age", "Age not set")
print(f"Age after removing it: {age}")
