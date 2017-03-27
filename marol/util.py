import os


def file_relative_path(relative_file, file_name):
    return os.path.join(os.path.dirname(relative_file), file_name)
