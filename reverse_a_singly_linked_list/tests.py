from .solve import *


def test1():
    node1 = Node(1)

    lst = SinglyLinkedList()
    lst.head = node1
    lst.reverse()
    assert lst.head.to_list() == [1]


def test2():
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2

    lst = SinglyLinkedList()
    lst.head = node1
    lst.reverse()
    assert lst.head.to_list() == [2, 1]


def test3():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3

    lst = SinglyLinkedList()
    lst.head = node1
    lst.reverse()
    assert lst.head.to_list() == [3, 2, 1]


def test4():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    lst = SinglyLinkedList()
    lst.head = node1
    lst.reverse()
    assert lst.head.to_list() == [4, 3, 2, 1]
