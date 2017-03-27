# -*- coding: utf-8 -*-
from . import helpers
from . import handler


def get_hmm():
    """Get a thought."""

    return helpers.marol_environment_path('3.6.0')


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


def get_lambda_files(py3_handler_file_path, version, tmp_python3_path='/tmp/handler_python3.py'):
    '''
    Constraints on the py3_handler
    * The handler functions should be named 'handler'
    * The file cannot be called handler
    * There should be no main statement in the handler file
    * One should not have the functions with the following names:
    ** load
    ** read_execution_uuid

    :param py3_handler_file_path:
    :return: a List of files and folders paths. The contents of the list are:
    * path to handler_python3.py. This is the renamed python file with code added in a tmp directory.
    * path to handler.py. This is the Python2 module that is called which delegates to the Python3 handler file
    * path to linux_venv folder. This is the folder which contains the virtual environment for the python version that you chose.
    '''

    helpers.write_handler_python3(py3_handler_file_path, tmp_python3_path)
    return [tmp_python3_path, handler.__file__, helpers.marol_environment_path(version)]
    pass
