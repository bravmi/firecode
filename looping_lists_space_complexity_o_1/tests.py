from .solve import *


def test5():
    node1 = Node(1)
    node4 = Node(4, node1)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1.next = node2

    lst = SinglyLinkedList(node1)
    assert lst.is_cyclic() is True


def test4():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    lst = SinglyLinkedList(node1)
    assert lst.is_cyclic() is False
