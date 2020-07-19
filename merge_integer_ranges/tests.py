from .solve import *


def test1():
    input_range_list = [[1, 10], [5, 8], [8, 15]]
    input_range_list = [Range(a[0], a[1]) for a in input_range_list]
    ranges = merge_ranges(input_range_list)
    assert [a.to_list() for a in ranges] == [[1, 15]]


def test2():
    input_range_list = [[5, 50], [25, 100], [150, 200]]
    input_range_list = [Range(a[0], a[1]) for a in input_range_list]
    ranges = merge_ranges(input_range_list)
    assert [a.to_list() for a in ranges] == [[5, 100], [150, 200]]


def test3():
    input_range_list = [[1, 5], [5, 10], [11, 15], [15, 20]]
    input_range_list = [Range(a[0], a[1]) for a in input_range_list]
    ranges = merge_ranges(input_range_list)
    assert [a.to_list() for a in ranges] == [[1, 10], [11, 20]]


def test4():
    input_range_list = [[1, 2], [2, 5], [8, 10], [15, 20]]
    input_range_list = [Range(a[0], a[1]) for a in input_range_list]
    ranges = merge_ranges(input_range_list)
    assert [a.to_list() for a in ranges] == [[1, 5], [8, 10], [15, 20]]


def test5():
    input_range_list = [[1, 4], [3, 7], [5, 10], [11, 15]]
    input_range_list = [Range(a[0], a[1]) for a in input_range_list]
    ranges = merge_ranges(input_range_list)
    assert [a.to_list() for a in ranges] == [[1, 10], [11, 15]]
