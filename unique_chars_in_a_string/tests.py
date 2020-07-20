from .solve import *


def test1():
    assert unique_chars_in_string("abcde") is True


def test2():
    assert unique_chars_in_string("aa") is False


def test3():
    assert unique_chars_in_string("") is True
