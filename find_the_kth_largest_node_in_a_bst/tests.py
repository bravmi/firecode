from .solve import *


def test1():
    node2 = TreeNode(2)

    node5 = TreeNode(5)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node5, node10)

    node4 = TreeNode(4, node2, node8)

    tree = BinaryTree(node4)
    assert tree.find_kth_largest(node4, 1).data == 10
    assert tree.find_kth_largest(node4, 2).data == 8
    assert tree.find_kth_largest(node4, 3).data == 5
    assert tree.find_kth_largest(node4, 4).data == 4
    assert tree.find_kth_largest(node4, 5).data == 2


def test2():
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)

    node5 = TreeNode(5)
    node4 = TreeNode(4, None, node5)

    node3 = TreeNode(3, node2, node4)

    tree = BinaryTree(node4)
    assert tree.find_kth_largest(node3, 1).data == 5
    assert tree.find_kth_largest(node3, 2).data == 4
    assert tree.find_kth_largest(node3, 3).data == 3
    assert tree.find_kth_largest(node3, 4).data == 2
    assert tree.find_kth_largest(node3, 5).data == 1


def test3():
    node2 = TreeNode(2)
    node1 = TreeNode(1, None, node2)

    tree = BinaryTree(node1)
    assert tree.find_kth_largest(node1, 1).data == 2
    assert tree.find_kth_largest(node1, 2).data == 1
