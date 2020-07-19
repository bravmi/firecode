from .solve import *


def test19():
    assert is_happy_number(19)


def test12():
    assert not is_happy_number(12)


def test100():
    assert is_happy_number(100)


def test68():
    assert is_happy_number(68)


def test28():
    assert is_happy_number(28)
