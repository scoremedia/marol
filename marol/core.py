# -*- coding: utf-8 -*-
from . import helpers
from . import handler
import os


def get_lambda_files(py3_handler_file_path, version, tmp_python3_path='/tmp/handler_python3.py', marol_home_path=None):
    '''
    Constraints on the py3_handler
    * The handler function should be named 'handler'
    * The file cannot be called handler
    * There should be no main statement in the handler file
    * One should not have the functions with the following names:
    ** load
    ** read_execution_uuid

    :param py3_handler_file_path:
    :return: a List of files and folders paths. The contents of the list are:
    * path to handler_python3.py. This is the renamed python file with code added in a tmp directory.
    * path to handler.py. This is the Python2 module that is called which delegates to the Python3 handler file
    * path to marol_venv folder. This is the folder which contains the virtual environment for the python version that you chose.
    '''

    assert os.path.basename(py3_handler_file_path) != 'handler.py', "Handler file name should" \
                                                                    " not be 'handler.py'. See README"

    predefined_error_string = """
    One of the following predefined statements were present and are not allowed
    * There should be no `if __name__ == '__main__':` statement
    * There should be no functions named load or read_execution_uuid
    """
    assert not helpers.predefined_functions_present(py3_handler_file_path), predefined_error_string

    handler_error_string = """
    A function named handler should be present in your handler file.
    """
    assert helpers.is_handler_function_present(py3_handler_file_path), handler_error_string

    helpers.write_handler_python3(py3_handler_file_path, tmp_python3_path)
    return [tmp_python3_path,
            handler.__file__,
            helpers.get_or_build_marol_environment_path(version, marol_home_path)]
    pass
