from .solve import *


def test1():
    node1 = Node(1, Node(2, Node(3)))
    l = SinglyLinkedList(node1)
    l.insert_at_pos(4, 2)
    assert l.to_list() == [1, 4, 2, 3]


def test2():
    node9 = Node(9, Node(1, Node(4, Node(2, Node(3)))))
    l = SinglyLinkedList(node9)
    l.insert_at_pos(8, 6)
    assert l.to_list() == [9, 1, 4, 2, 3, 8]


def test3():
    l = SinglyLinkedList()
    l.insert_at_pos(4, 1)
    assert l.to_list() == [4]


def test4():
    node1 = Node(1, Node(4, Node(2, Node(3))))
    l = SinglyLinkedList(node1)
    l.insert_at_pos(9, 1)
    assert l.to_list() == [9, 1, 4, 2, 3]
