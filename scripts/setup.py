import sys
import os

path = os.path.realpath(os.path.dirname(__file__))
path1 = os.path.normpath(os.path.join(path, '..'))

sys.path.append(path1)
