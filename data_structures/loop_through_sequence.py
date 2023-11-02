# Here we're looping through a list
fruit_list = ["Apple", "Banana", "Orange"]
for fruit in fruit_list:
    print(fruit)

student_count = {
    "course1": 923,
    "course2": 7738,
    "course3": 112,
}

# We're going to loop through dictionary values
for k, v in student_count.items():
    print(f"{k}: {v}")

# Count the total number of students
total_students = 0
for k, v in student_count.items():
    total_students += v

print(f"Total students: {total_students}")

# Get all keys from dictionary
# dict_keys(['course1', 'course2', 'course3'])
courses = student_count.keys()
print(courses)
