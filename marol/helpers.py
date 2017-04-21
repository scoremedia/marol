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
        path = os.path.join(home_path, DEFAULT_HOME)
    else:
        path = os.environ['MAROL_HOME']

    os.makedirs(path, exist_ok=True)
    return path


def build_marol_environment(python_version):
    staging_tar_path = download_source(python_version)
    build_environment(staging_tar_path, python_version)

    pass


def build_environment(staging_tar_path, python_version):
    src_path = '/src'
    image = 'lambci/lambda:build'

    client = docker.from_env()

    volume_bindings = {
        staging_tar_path: {
            'bind': src_path,
            'mode': 'rw',
        },
    }

    python_main_version = python_version.rpartition('.')[0]
    python_version_root = python_version.partition('.')[0]

    commands = [
        'rm -rf marol_venv/',
        'rm -rf Python-{python_version}'.format(python_version=python_version),
        'tar xfz Python-{python_version}.tgz'.format(python_version=python_version),
        'cd Python-{python_version}'.format(python_version=python_version),
        './configure',
        'make',
        'make install',
        'cd ..',
        'pip3 install virtualenv',
        'virtualenv -p /usr/local/bin/python{python_version_root} marol_venv'.format(
            python_version_root=python_version_root),
        'rm -rf marol_venv/lib/python{python_main_version}/'.format(python_main_version=python_main_version),
        'cp -rf /usr/local/lib/python{python_main_version} marol_venv/lib/'.format(
            python_main_version=python_main_version),
        'find . -name __pycache__ -type d -exec rm -rf {} +',
        'rm marol_venv/include/python{python_main_version}m'.format(python_main_version=python_main_version),
        'cp -rf /usr/local/include/python{python_main_version}m marol_venv/include/'.format(
            python_main_version=python_main_version)
    ]
    command_str = ' && '.join(commands)
    command_line = ['sh', '-c', command_str]
    client.containers.run(image=image,
                          command=command_line,
                          volumes=volume_bindings,
                          working_dir=src_path)

    pass


def download_source(python_version):
    home_path = determine_home_path()
    python_server_tar_path = PYTHON_TAR_TEMPLATE.format(python_version=python_version)
    staging_area_path = os.path.join(home_path, STAGING_PATH, python_version)
    os.makedirs(staging_area_path, exist_ok=True)
    staging_tar_path = os.path.join(staging_area_path, FILE_NAME_TEMPLATE.format(python_version=python_version))
    urllib.request.urlretrieve(python_server_tar_path,
                               staging_tar_path)
    return staging_area_path
