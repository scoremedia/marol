import setup
from marol import build_marol_environment
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--python_version", required=True)
    args = parser.parse_args()
    build_marol_environment(args.python_version)
