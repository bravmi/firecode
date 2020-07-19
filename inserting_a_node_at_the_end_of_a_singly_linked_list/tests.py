from .solve import *


def test1():
    node1 = Node()
    node1.setData(1)
    node2 = Node()
    node2.setData(2)
    node1.setNext(node2)
    assert node1.getNext().getData() == 2


def test2():
    lst = SinglyLinkedList()
    lst.insertAtEnd(1)
    lst.insertAtEnd(2)
    lst.insertAtEnd(3)
    assert lst.to_list() == [1, 2, 3]
