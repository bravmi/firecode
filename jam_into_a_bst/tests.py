from .solve import *


def test1():
    node2 = TreeNode(2)

    node5 = TreeNode(5)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node5, node10)

    node4 = TreeNode(4, node2, node8)

    tree = BinaryTree()
    tree.insert(node4, 6)
    assert tree.to_list(node4) == [4, 2, 8, 5, 6, 10]


def test2():
    tree = BinaryTree()
    assert tree.root is None


def test3():
    node1 = TreeNode(1)

    tree = BinaryTree()
    tree.insert(node1, 2)
    tree.insert(node1, 3)
    assert node1.right_child.right_child.data == 3


def test4():
    node1 = TreeNode(1)

    tree = BinaryTree()
    tree.insert(node1, 2)
    tree.insert(node1, 3)
    tree.insert(node1, 4)
    tree.insert(node1, 5)
    tree.insert(node1, 6)
    tree.insert(node1, 7)
    assert tree.to_list(node1) == [1, 2, 3, 4, 5, 6, 7]


def test5():
    node4 = TreeNode(4)

    tree = BinaryTree()
    tree.insert(node4, 2)
    tree.insert(node4, 8)
    tree.insert(node4, 5)
    tree.insert(node4, 10)
    assert tree.to_list(node4) == [4, 2, 8, 5, 10]
