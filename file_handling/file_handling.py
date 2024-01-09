import os

_TARGET_FILE = 'target.txt'

def write_file(filename, content):
    """Write content to new file."""
    with open(filename, "w") as file_object:
        file_object.write(content)
    return f"Content written to '{filename}'."

def read_file(filename):
    """Read content from existing file."""
    try:
        with open(filename, "r") as file_object:
            content = file_object.read()
            return content
    except FileNotFoundError:
        return f"'{filename}' does not exist."


def append_file(filename, content):
    """Append content to existing file."""
    with open(filename, "a") as file_object:
        file_object.write(content)
    return f"Content appended to '{filename}'."
    

def delete_file(_TARGET_FILE):
    """Delete file"""
    os.remove(_TARGET_FILE)
    return f"'{_TARGET_FILE}' has been deleted."

def main():
    result = write_file(_TARGET_FILE, "This is a test.")
    assert result == f"Content written to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test."

    append_result = append_file(_TARGET_FILE, "\nThis is an appended line.")
    assert append_result == f"Content appended to '{_TARGET_FILE}'."

    content = read_file(_TARGET_FILE)
    assert content == "This is a test.\nThis is an appended line."

    delete_result = delete_file(_TARGET_FILE)
    assert delete_result == f"'{_TARGET_FILE}' has been deleted."


if __name__ == "__main__":
    main()