import pathlib


def get_file_dir(file):
    return pathlib.Path(file).parent.resolve()
