from .solve import *


def test1():
    assert is_power_of_four(5) is False


def test2():
    assert is_power_of_four(16) is True


def test3():
    assert is_power_of_four(12) is False
