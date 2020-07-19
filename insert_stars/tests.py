from .solve import *


def test1():
    assert insert_star_between_pairs('cac') == 'cac'


def test2():
    assert insert_star_between_pairs('cc') == 'c*c'


def test3():
    assert insert_star_between_pairs('bbb') == 'b*b*b'


def test4():
    assert insert_star_between_pairs('') == ''


def test5():
    assert insert_star_between_pairs('abba') == 'ab*ba'
