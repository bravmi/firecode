from .solve import *


def test1():
    assert excel_column_name_to_number('A') == 1


def test2():
    assert excel_column_name_to_number('AA') == 27


def test3():
    assert excel_column_name_to_number('ABC') == 731


def test4():
    assert excel_column_name_to_number('ABCD') == 19010


def test5():
    assert excel_column_name_to_number('ABCDZ') == 494286
