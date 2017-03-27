import inspect
from textwrap import dedent
import shutil

from . import project
from . import handler_python3_meta as meta
import os


def get_answer():
    """Get an answer."""
    return True


def write_handler_python3(py3_handler_file_path, tmp_python3_path):
    shutil.copyfile(py3_handler_file_path, tmp_python3_path)
    main_starter_code = """
    if __name__ == '__main__':
        main()
    """
    code_strs = [inspect.getsource(f) for f in [meta.load, meta.read_execution_uuid, meta.main]]
    all_code_strs = code_strs + [dedent(main_starter_code)]
    with open(tmp_python3_path, 'a') as f:
        for code_str in all_code_strs:
            f.write('\n')
            f.write(code_str)


def marol_environment_path(version):
    path = project.root() + '/environments/{version}/marol_venv'.format(version=version)
    if os.path.exists(path):
        return path
    else:
        raise ValueError(
            'Python Version:{version} is not supported. Contact project committers.'.format(version=version))
    return path
