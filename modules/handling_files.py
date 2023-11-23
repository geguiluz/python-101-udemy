"""Handling files using imports and custom module for file handling"""

from files import file_handler as fh

fh.write_file("test_file.txt", "output", "Other contents", "w")

print(fh.open_file("test_file.txt", "output"))
