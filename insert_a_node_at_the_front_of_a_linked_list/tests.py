from .solve import *


def test1():
    lst = SinglyLinkedList()
    lst.insert_at_front(1)
    lst.insert_at_front(2)
    lst.insert_at_front(3)
    assert lst.to_list() == [3, 2, 1]
