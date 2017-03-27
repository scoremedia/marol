from subprocess import PIPE, Popen
import uuid
import os
from pprint import pprint
import pickle


class Context(object):
    def __init__(self, context):
        self.function_name = context.function_name
        self.function_version = context.function_version
        self.invoked_function_arn = context.invoked_function_arn
        self.memory_limit_in_mb = context.memory_limit_in_mb
        self.aws_request_id = context.aws_request_id
        self.log_group_name = context.log_group_name
        self.log_stream_name = context.log_stream_name

    def __getstate__(self):
        return self.__dict__

    def __set_state__(self, d):
        self.__dict__ = d


def dump(python_object, path):
    pickle.dump(python_object, open(path, "wb"))


def handler(event, context):
    execution_uuid = uuid.uuid4()
    event_path = '/tmp/event_{}'.format(execution_uuid)
    dump(event, event_path)
    context_path = '/tmp/context_{}'.format(execution_uuid)
    dump(Context(context), context_path)

    commands = '''
    marol_venv/bin/python ./handler_python3.py --execution_uuid {ex_uuid}
    '''.format(ex_uuid=str(execution_uuid))

    p = Popen('/bin/bash', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
    stdout, stderr = p.communicate(commands)
    pprint(stdout)
    pprint(stderr)

    os.remove(event_path)
    os.remove(context_path)
