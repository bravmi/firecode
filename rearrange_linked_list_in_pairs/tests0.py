from .solve0 import *


def test1():
    node1 = Node(1, Node(2, Node(3, Node(4))))
    l = SinglyLinkedList(node1)
    l.arrange_in_pairs()
    assert l.to_list() == [1, 4, 2, 3]


def test2():
    node1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    l = SinglyLinkedList(node1)
    l.arrange_in_pairs()
    assert l.to_list() == [1, 5, 2, 4, 3]


def test3():
    l = SinglyLinkedList(None)
    l.arrange_in_pairs()
    assert l.to_list() == []


def test4():
    node1 = Node(1)
    l = SinglyLinkedList(node1)
    assert l.to_list() == [1]
