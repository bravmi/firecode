from .solve import *


def test1():
    input_list = [1, 2, 5, 5, 8, 8, 10]
    input_number = 8
    assert str(find_range(input_list, input_number)) == '[4,5]'


def test2():
    input_list = [1, 2, 5, 5, 8, 8, 10]
    input_number = 2
    assert str(find_range(input_list, input_number)) == '[1,1]'


def test3():
    input_list = [1, 1, 1, 1]
    input_number = 1
    assert str(find_range(input_list, input_number)) == '[0,3]'
