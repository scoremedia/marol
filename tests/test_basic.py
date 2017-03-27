# -*- coding: utf-8 -*-

from .context import marol
import unittest
import os


def file_relative_path(relative_file, file_name):
    return os.path.join(os.path.dirname(relative_file), file_name)


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        print(marol.get_lambda_files(marol.project.root() + '/tests/data/dummy_handler.py', '3.6.0'))
        assert True


if __name__ == '__main__':
    unittest.main()
