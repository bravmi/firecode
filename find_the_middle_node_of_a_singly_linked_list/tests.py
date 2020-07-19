from .solve import *


def test1():
    node1 = Node()
    node1.data = 1

    lst = SinglyLinkedList()
    lst.head = node1
    assert lst.find_middle_node().data == 1


def test2():
    node1 = Node()
    node1.data = 1
    node2 = Node()
    node2.data = 2
    node1.next = node2

    lst = SinglyLinkedList()
    lst.head = node1
    assert lst.find_middle_node().data == 1


def test3():
    node1 = Node()
    node1.data = 1
    node2 = Node()
    node2.data = 2
    node1.next = node2
    node3 = Node()
    node3.data = 3
    node2.next = node3

    lst = SinglyLinkedList()
    lst.head = node1
    assert lst.find_middle_node().data == 2


def test4():
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
    assert lst.find_middle_node().data == 2


def test5():
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
    assert lst.find_middle_node().data == 3
