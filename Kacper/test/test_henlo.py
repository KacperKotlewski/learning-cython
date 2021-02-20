import pytest

from henlo.subpkg import util
from henlo import wrapper

def test__chars_type():
    res = util._chars("test")
    if type(res) != bytes:
        assert type(res) != bytes
def test__chars_value():
    res = util._chars("test")
    if res != b"test":
        assert res != b"test"