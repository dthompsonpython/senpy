import shutil
import os
import pytest


try:
    pytest.main(["-x", "tests/examples"])
except():
    pass
shutil.rmtree("dojo")
os.mkdir("dojo")
open("dojo/dojo.py", "w+").close()
open("dojo/__init__.py","w+").close()
