import os
import json


def _set_dir_path(sub_dir: str):
    """
    Outputs the full path under current working directory with the
    specified sub-directory name.
    """
    # Get current working directory
    base_dir = os.getcwd()
    full_dir_path = os.path.join(base_dir, sub_dir)
    print(full_dir_path)
    return full_dir_path


def gen_full_file_path(file_name: str, sub_dir: str):
    """Returns full file path and file name"""
    full_dir_path = _set_dir_path(sub_dir)
    os.makedirs(full_dir_path, exist_ok=True)
    # function os.path.join() creates the full path with our filename
    file_path = os.path.join(full_dir_path, file_name)
    return file_path


def write_file(
    file_name: str,
    sub_dir: str,
    contents: any,
    mode: str = "a",
    end_with_return: bool = "True",
):
    """
    Writes to a file with a given file_name inside sub_dir under cwd.

    Depending on the mode we use, we will get the following results
    w: Overrides existing content
    a: Appends to existing contents (same line)

    If we want to add content in the same line, we must add argument
    end_with_return="False" otherwise new line defaults to True.
    """

    file_path = gen_full_file_path(file_name, sub_dir)

    # Set line end
    if end_with_return:
        line_end = "\n"
    else:
        line_end = ""

    # Create file
    with open(file_path, mode) as msg_file:
        msg_file.write(contents + line_end)


def open_file(file_name: str, sub_dir: str):
    """
    Opens a file with a given file_name inside sub_dir under cwd.
    """
    file_path = gen_full_file_path(file_name, sub_dir)

    # Here we're reading the contents of the file and saving it to a variable 'msg'
    with open(file_path) as msg_file:
        msg = msg_file.read()
        print(msg)
    return msg


def open_json_file(file_name: str, sub_dir: str):
    """
    Opens a file with a given file_name inside sub_dir under cwd.
    """
    file_path = gen_full_file_path(file_name, sub_dir)

    with open(file_path) as f:
        # load() converts a json file to a dictionary
        json_data = json.load(f)
    return json_data
