# Marol

Marol enables you to run Python 3 code on AWS Lambda. 

## Python 3 version support

* Supports 3.6.0


## Instructions
You pass in your handler file(e.g. `my_handler.py`) and it returns back:

* `handler_python3.py`. `my_handler.py` is renamed to `handler_python3.py` and code is added to make it callable from a python2 handler
* `handler.py`. This is the Python2 module that is called which delegates to the Python3 handler file
* path to `marol_venv` folder. This is the folder which contains all the executables for the Python version that you chose.

To use Marol, your `my_handler.py` will have to have the following constraints:

* The handler function should be named `handler`
* The file cannot be called `handler.py`(This is reserved for the Python2 handler which will execute the Python3 handler
* There should be no `main` statement in the handler file
* One should not have functions with the following names:
   1. `load`
   2. `read_execution_uuid`


## Installation

Since it is a private repo for now, you can install it by

```
pip install git+ssh://git@github.com/scoremedia/marol.git

```
or ..
### requirements.txt

Add the following line to your `requirements.txt` file

```
-e git+ssh://git@github.com/scoremedia/marol.git#egg=marol
```

## Usage

```python
import marol
my_project_site_packages = ...
deploy_lambda('production',
              lambda_name,
              marol.get_lambda_files('~/mypath/mypy3handler.py', '3.6.0') + my_project_site_packages,
              'lambda_s3_exec_role',
              128,
              300,
              lambda_description='Test for Python 3',
              handler_name="handler",
              region_name='us-east-1')

```
