from .solve import *
from .solve_alt import generate_ip_address as generate_ip_address_alt


def test1():
    s = '0001'
    assert generate_ip_address(s) == ['0.0.0.1'] == generate_ip_address_alt(s)


def test2():
    s = '0010'
    assert generate_ip_address(s) == ['0.0.1.0'] == generate_ip_address_alt(s)


def test3():
    s = '25525511135'
    assert (
        generate_ip_address(s)
        == ['255.255.11.135', '255.255.111.35']
        == generate_ip_address_alt(s)
    )


def test4():
    s = '1921682040'
    assert (
        generate_ip_address(s)
        == [
            '19.216.82.040',
            '192.16.82.040',
            '192.168.2.040',
            '192.168.20.40',
            '192.168.204.0',
        ]
        == generate_ip_address_alt(s)
    )
