from .solve import *


def test1():
    node1 = Node()
    node1.data = 1
    node2 = Node()
    node2.data = 2
    node1.next = node2
    node3 = Node()
    node3.data = 3
    node2.next = node3
    node4 = Node()
    node4.data = 4
    node3.next = node4

    lst = SinglyLinkedList()
    lst.head = node1
    assert lst.is_list_even() is True


def test2():
    node1 = Node()
    node1.data = 1
    node2 = Node()
    node2.data = 2
    node1.next = node2
    node3 = Node()
    node3.data = 3
    node2.next = node3
    node4 = Node()
    node4.data = 4
    node3.next = node4
    node5 = Node()
    node5.data = 5
    node4.next = node5

    lst = SinglyLinkedList()
    lst.head = node1
    assert lst.is_list_even() is False
