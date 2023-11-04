"""
This code will get the path of current project and will create a
directory for output files
"""
import os

# Get current working directory
base_dir = os.getcwd()
sub_dir = "output"
full_fir_path = os.path.join(base_dir, sub_dir)
print(full_fir_path)

# Flag exist_ok=True prevents code from erroring ig directory already exists
os.makedirs(full_fir_path, exist_ok=True)

# function os.path.join() creates the full path with our filename
file_path = os.path.join(full_fir_path, "message.txt")
with open(file_path, "a") as msg_file:
    msg_file.write("Hello\n")
