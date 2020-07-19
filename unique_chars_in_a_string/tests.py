from .solve import *


def test1():
    assert unique_chars_in_string("abcde") == True


def test2():
    assert unique_chars_in_string("aa") == False


def test3():
    assert unique_chars_in_string("") == True
