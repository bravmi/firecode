from .solve import *

# make_palindrome = make_palindrome_rec


def test1():
    assert make_palindrome('race') == 'racecar'


def test2():
    assert make_palindrome('abc') == 'abcba'


def test3():
    assert make_palindrome('rad') == 'radar'


def test4():
    assert make_palindrome('aba') == 'aba'


def test5():
    assert make_palindrome('madam') == 'madam'
