import argparse
import shutil
import os
import pytest


parser = argparse.ArgumentParser(description='Senpy noticed you.')
parser.add_argument('testname', metavar='name', type=str,
                    help='test name')

args = parser.parse_args()

try:
    pytest.main(["-x", "tests/{}".format(args.testname)])
except():
    pass
shutil.rmtree("dojo")
os.mkdir("dojo")
open("dojo/dojo.py", "w+").close()
open("dojo/__init__.py","w+").close()
