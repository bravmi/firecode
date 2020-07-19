from .solve import *


def test1():
    assert match("fi*de", "firecode") is True


def test2():
    assert match("fi?de", "firecode") is False


def test3():
    assert match("fi*de", "firecodede") is True


def test4():
    assert match("*", "firecodede") is True


def test5():
    assert match("?", "firecodede") is False


def test6():
    assert match("fi*d?", "firecode") is True


def test7():
    assert match("*i*d?", "fabfirecode") is True


def test8():
    assert match("fir?code", "firecode") is True


def test9():
    assert match("fi*de", "firecode") is True


def test10():
    assert match("*i?e*d?", "firecode") is True


def test11():
    assert match("fi*d?", "firecodee") is False


def test12():
    assert match("fi?de", "firecode") is False


def test13():
    assert match("?i?e*d?", "fairecode") is False


def test14():
    assert match("fi*de*s", "firecodes") is True
