from .solve import *


def test1():
    assert decode_string('521') == 2


def test2():
    assert decode_string('113021') == 0


def test3():
    assert decode_string('29') == 1


def test4():
    assert decode_string('2202') == 1


def test5():
    assert decode_string('21234') == 5
