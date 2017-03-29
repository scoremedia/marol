import inspect
from textwrap import dedent
import shutil
from . import project
from . import handler_python3_meta as meta
import os
import docker
import urllib.request

DEFAULT_HOME = '.marol'
PYTHON_TAR_TEMPLATE = 'https://www.python.org/ftp/python/{python_version}/Python-{python_version}.tgz'
FILE_NAME_TEMPLATE = 'Python-{python_version}.tgz'
STAGING_PATH = 'staging'


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


def determine_home_path():
    if 'MAROL_HOME' not in os.environ:
        if 'HOME' in os.environ:
            home_path = os.environ['HOME']
        else:
            home_path = os.path.expanduser('~')
        return os.path.join(home_path, DEFAULT_HOME)
    else:
        return os.environ['MAROL_HOME']


def build_marol_environment(python_version):
    home_path = determine_home_path()
    os.makedirs(home_path, exist_ok=True)
    python_tar_path = PYTHON_TAR_TEMPLATE.format(python_version=python_version)
    staging_path = os.path.join(home_path, STAGING_PATH, python_version)

    os.makedirs(staging_path, exist_ok=True)
    urllib.request.urlretrieve(python_tar_path,
                               os.path.join(staging_path,
                                            FILE_NAME_TEMPLATE.format(python_version=python_version)))

    pass
