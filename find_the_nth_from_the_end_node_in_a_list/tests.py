from .solve import *


def test1():
    node6 = Node(6)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    list_ = SinglyLinkedList(node1)
    assert list_.find_nth_node_from_end(2).data == 5


def test2():
    list_ = SinglyLinkedList()
    assert list_.find_nth_node_from_end(0) is None


def test3():
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    list_ = SinglyLinkedList(node1)
    assert list_.find_nth_node_from_end(-1) is None
