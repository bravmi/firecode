from .solve import *


def test1():
    assert distributeChocolateBrute([1, 5, 7, 1]) == 7
    assert distributeChocolate([1, 5, 7, 1]) == 7


def test2():
    assert distributeChocolateBrute([]) == 0
    assert distributeChocolate([]) == 0


def test3():
    assert distributeChocolateBrute([2]) == 1
    assert distributeChocolate([2]) == 1


def test4():
    assert distributeChocolateBrute([2, 3, 3, 2, 1, 5, 2]) == 12
    assert distributeChocolate([2, 3, 3, 2, 1, 5, 2]) == 12
