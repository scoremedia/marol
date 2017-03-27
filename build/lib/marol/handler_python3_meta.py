def read_execution_uuid():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--execution_uuid", required=True)
    args = parser.parse_args()

    return args.execution_uuid


def load(path):
    import pickle
    return pickle.load(open(path, "rb"))


def handler(event, context):
    pass


def main():
    execution_uuid = read_execution_uuid()
    event_path = '/tmp/event_{}'.format(execution_uuid)
    context_path = '/tmp/context_{}'.format(execution_uuid)
    event = load(event_path)
    context = load(context_path)
    handler(event, context)


if __name__ == '__main__':
    main()
