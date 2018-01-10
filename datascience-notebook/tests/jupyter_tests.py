from jupyter_wrapper import _notebook_run
import os

TEST_DIR = os.environ['TEST_DIR']


def test_py2kernel():
    nb, errors = _notebook_run(TEST_DIR + 'python2_test.ipynb')
    assert errors == []


def test_py3kernel():
    nb, errors = _notebook_run(TEST_DIR + 'python3_test.ipynb')
    assert errors == []
