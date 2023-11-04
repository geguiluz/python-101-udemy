import os

# Get current working directory
base_dir = os.getcwd()
sub_dir = "output"
full_dir_path = os.path.join(base_dir, sub_dir)
print(full_dir_path)
os.makedirs(full_dir_path, exist_ok=True)

file_path = os.path.join(full_dir_path, "numbers.txt")

with open(file_path, "w") as num_file:
    for num in range(1, 1000001):
        num_file.write(f"{num}\n")

print("Finished creating large file.")
