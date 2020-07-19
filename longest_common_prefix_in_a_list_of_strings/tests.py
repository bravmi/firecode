from .solve import *


def test1():
    items = ['firecode', 'fireacb', 'fireac']
    assert long_common_prefix(items) == 'fire'


def test2():
    items = ['firecode', 'fireacb', 'firac', 'firca', 'firecab', 'firecba']
    assert long_common_prefix(items) == 'fir'


def test3():
    items = ['firecode', 'fireacb', 'firac', 'rcafir', 'firecab', 'firecba']
    assert long_common_prefix(items) == ''


def test4():
    items = ['airecode', 'aireacb', 'airac', 'airca', 'airecab', 'airecba']
    assert long_common_prefix(items) == 'air'
