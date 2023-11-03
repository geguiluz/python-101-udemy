file_path = "message.txt"

# Here we're reading the contents of the file and saving it to a variable 'msg'
with open(file_path) as msg_file:
    msg = msg_file.read()

print(msg)
