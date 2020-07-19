from .solve import *


def test1():
    ranges = [[1, 4], [3, 7], [5, 10], [11, 15]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(7, 8))
    assert [a.to_list() for a in ranges] == [[1, 10], [11, 15]]


def test2():
    ranges = [[1, 10], [5, 8], [8, 15]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(9, 20))
    assert [a.to_list() for a in ranges] == [[1, 20]]


def test3():
    ranges = [[1, 2], [2, 5], [8, 10], [15, 20]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(11, 14))
    assert [a.to_list() for a in ranges] == [
        [1, 5],
        [8, 10],
        [11, 14],
        [15, 20],
    ]


def test4():
    ranges = [[1, 5], [5, 10], [11, 15], [15, 20]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(25, 30))
    assert [a.to_list() for a in ranges] == [[1, 10], [11, 20], [25, 30]]


def test5():
    ranges = [[5, 50], [25, 100], [150, 200]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(120, 140))
    assert [a.to_list() for a in ranges] == [[5, 100], [120, 140], [150, 200]]


def test6():
    ranges = [[3, 5], [5, 10], [11, 15], [15, 20]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(1, 2))
    assert [a.to_list() for a in ranges] == [[1, 2], [3, 10], [11, 20]]


def test7():
    ranges = [[1, 4], [3, 7], [5, 10], [11, 15]]
    ranges = [Range(*a) for a in ranges]
    ranges = insert_and_merge(ranges, Range(7, 8))
    assert [a.to_list() for a in ranges] == [[1, 10], [11, 15]]
