from .solve import *


def test3():
    a = [1, 2, 3, 6, 7, 8, 10, 11]
    ranges1 = [
        range_format(r) for r in [Range(1, 3), Range(6, 8), Range(10, 11)]
    ]
    ranges2 = find_partitions(a)
    assert ranges2 == ranges1


def test2():
    a = [1, 3]
    ranges1 = [range_format(r) for r in [Range(1, 1), Range(3, 3)]]
    ranges2 = find_partitions(a)
    assert ranges2 == ranges1


def test0():
    a = []
    assert [range_format(r) for r in find_partitions(a)] == []


def test1():
    a = [1]
    ranges1 = [range_format(r) for r in [Range(1, 1)]]
    ranges2 = find_partitions(a)
    assert ranges2 == ranges1


def test15():
    a = [1, 2, 3, 4, 5]
    ranges1 = [range_format(r) for r in [Range(1, 5)]]
    ranges2 = find_partitions(a)
    assert ranges2 == ranges1
