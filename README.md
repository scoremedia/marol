# Disclaimer
* theScore does not use this in production. This library was built when AWS Lambda was stuck at 2.7 for a long time and we wanted to use Python 3. Two days after this idea succeeded, AWS announced support for 3.6 :). However, this may still be of use to those who want to use versions other than the official version

# Marol

Run any Python 3 version instead of the standard AWS Lambda Python version.

## Python 3 version support

* Tested on 3.6.1 and 3.6.2


## Instructions
You pass in your handler file(e.g. `my_handler.py`) and it returns back:

* `handler_python3.py`. `my_handler.py` is renamed to `handler_python3.py` and code is added to make it callable from a python2 handler
* `handler.py`. This is the Python2 module that is called which delegates to the Python3 handler file
* path to `marol_venv` folder. This is the folder which contains all the executables for the Python version that you chose.

To use Marol, your `my_handler.py` will have the following constraints:

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


## Usage

Your deployment scripts for lambda should specify `handler.py` and `handler` as the starting point for your Lambda function. This is the Python2 handler returned by Marol which calls your modified Python3 handler.


```python
import marol
my_project_site_packages = ...
my_deploy_lambda_function(lambda_name,
                          marol.get_lambda_files('~/mypath/mypy3handler.py', '3.6.1') + my_project_site_packages,
                          'lambda_s3_exec_role',
                          128,
                          300,
                          lambda_description='Test for Python 3',
                          handler_name="handler",
                          region_name='us-east-1')

```

`get_lambda_files` will check `MAROL_HOME` if `marol_venv` works for the particular version that you want. If it exists, you will get back that path. If it does not exist,`marol` 
* download the python source
* build the binaries in [docker image](https://github.com/lambci/docker-lambda) which mirrors the AWS Lambda Environment
* create a basic `marol_venv` and store it at `MAROL_HOME`

## Future Work
* Some of the context attributes are not supported yet.
* Ensure that the context object is updated for future changes

## Notes
* Default Marol home is `<HOME>/.marol`. 
* It will create `marol_venv` in `<HOME>/.marol/staging/<python_version>`


## Notes for those thinking about security
* This uses an unofficial [docker image](https://github.com/lambci/docker-lambda)
