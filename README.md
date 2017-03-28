Marol
========================

Marol enables you to run Python 3 code on Lambda. You pass in your handler file(e.g. my_handler.py) and it returns back:
    * handler_python3.py. `my_handler.py` is renamed to `handler_python3.py` and code is added to make it callable from a python2 handler
    * handler.py. This is the Python2 module that is called which delegates to the Python3 handler file
    * path to marol_venv folder. This is the folder which contains all the executables for the Python version that you chose.

To use Marol, your `my_handler.py` will have to have the following constraints
    * The handler function should be named 'handler'
    * The file cannot be called handler.py(This is reserved for the Python2 handler which will execute the Python3 handler
    * There should be no main statement in the handler file
    * One should not have functions with the following names:
        ** load
        ** read_execution_uuid
