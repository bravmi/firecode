from .solve import *


def test4():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    lst = SinglyLinkedList(node1)
    assert lst.to_list() == [1, 2, 3, 4]
    lst.delete(3)
    assert lst.to_list() == [1, 2, 4]


def test1():
    node1 = Node(1)

    lst = SinglyLinkedList(node1)
    assert lst.to_list() == [1]
    lst.delete(1)
    assert lst.to_list() == []


def test3():
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    lst = SinglyLinkedList(node1)
    assert lst.to_list() == [1, 2, 3]
    lst.delete(1)
    assert lst.to_list() == [2, 3]


def test0():
    lst = SinglyLinkedList()
    assert lst.to_list() == []
    lst.delete(3)
    assert lst.to_list() == []
