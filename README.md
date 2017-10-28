# Marol

Run any Python 3 version instead of the standard AWS Lambda Python version.

## Python 3 version support

* Currently supports 3.6.1 +


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
### Pre-requisites
* Ensure `docker` is installed and running on the machine where Marol is executed.

### Mac OS X
* Open the terminal and run `/Applications/<Python Version>/Install Certificates.command` 

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

Your deployment scripts for lambda should specify `handler.py` and `handler` as the starting point for your Lambda function. This is the Python2 handler returned by Marol which calls your modified Python3 handler.


```python
import marol
my_project_site_packages = ...
deploy_lambda('production',
              lambda_name,
              marol.get_lambda_files('~/mypath/mypy3handler.py', '3.6.1') + my_project_site_packages,
              'lambda_s3_exec_role',
              128,
              300,
              lambda_description='Test for Python 3',
              handler_name="handler",
              region_name='us-east-1')

```


## Future Work
* Some of the context attributes are not supported yet.
* Ensure that the context object is updated for future changes

## Notes
* Working Call: `./scripts/marol-build.py`
* It will create `marol_venv` in `~/.marol/staging/<python_version>`
* Right now, to make it work, we have to copy `~/.marol/staging/<python_version>/marol_venv` to `marol/environments/<python_version>/marol_venv`


## Notes for those thinking about security
* This uses the docker image: https://github.com/lambci/docker-lambda
* Marol will download the Python Source and build it and place it in `MAROL_HOME` if defined or `~/.marol` on Unix systems