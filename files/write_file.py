file_path = "output.txt"

text_lines = [
        "Hello\n",
        "My name is \n"
        "Memo",
]

""" 
Depending on the mode we use, we will get the following results
w: Overrides existing content
a: Appends to existing contents (same line)

If we want to add content in a new line, we must add a \n at the
end of each content line.

"""

# This example writes a single line to a file
with open(file_path, 'a') as out_file:
    out_file.write("File contents\n")

# This example write multiple lines to a file
with open(file_path, 'a') as out_file:
    out_file.writelines(text_lines)


