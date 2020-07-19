from .solve import *


def test1():
    assert largestContinuousSum([-1, -2, 3, 4, 5]) == 12


def test2():
    assert largestContinuousSum([-8, -2, -1, -9, -2, -4]) == -1


def test3():
    assert (
        largestContinuousSum([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
        == 187
    )


def test4():
    assert largestContinuousSum([1, 2, 3]) == 6


def test5():
    assert largestContinuousSum([0, -2, -1, -3]) == 0


def test6():
    assert largestContinuousSum([]) == None
