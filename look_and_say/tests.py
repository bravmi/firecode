from .solve import *


def test0():
    assert look_and_say(0) == None


def test1():
    assert look_and_say(1) == 1


def test2():
    assert look_and_say(2) == 11


def test3():
    assert look_and_say(3) == 21


def test4():
    assert look_and_say(4) == 1211


def test5():
    assert look_and_say(5) == 111221
