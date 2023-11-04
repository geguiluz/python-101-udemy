import os

sum_of_nums = 0

# Get current working directory
base_dir = os.getcwd()
sub_dir = "output"
full_dir_path = os.path.join(base_dir, sub_dir)
print(full_dir_path)
os.makedirs(full_dir_path, exist_ok=True)

file_path = os.path.join(full_dir_path, "numbers.txt")

with open(file_path) as nf:
    for num in nf:
        # Read the number from file and cast into integer
        sum_of_nums += int(num)

print(sum_of_nums)
