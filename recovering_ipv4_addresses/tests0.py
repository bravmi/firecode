from .solve0 import *


def test1():
    assert generate_ip_address('0001') == ['0.0.0.1']


def test2():
    assert generate_ip_address('0010') == ['0.0.1.0']


def test3():
    assert generate_ip_address('25525511135') == [
        '255.255.11.135',
        '255.255.111.35',
    ]


def test4():
    assert generate_ip_address('1921682040') == [
        '19.216.82.040',
        '192.16.82.040',
        '192.168.2.040',
        '192.168.20.40',
        '192.168.204.0',
    ]
