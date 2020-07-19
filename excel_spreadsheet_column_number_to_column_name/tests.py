from .solve import *


def test1():
    assert excel_column_number_to_name(27) == 'AA'


def test2():
    assert excel_column_number_to_name(494286) == 'ABCDZ'


def test3():
    assert excel_column_number_to_name(19010) == 'ABCD'


def test4():
    assert excel_column_number_to_name(26) == 'Z'


def test5():
    assert excel_column_number_to_name(1) == 'A'


def test6():
    assert excel_column_number_to_name(52) == 'AZ'


def test7():
    assert excel_column_number_to_name(731) == 'ABC'
