from .solve import *


def test1():
    node5 = TreeNode(5)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node5, node10)
    node2 = TreeNode(2)
    node4 = TreeNode(4, node2, node8)

    tree = BinaryTree(node4)
    assert tree.find_kth_smallest(tree.root, 2).data == 4


def test2():
    node2 = TreeNode(2)
    node4 = TreeNode(4, node2)

    node10 = TreeNode(10)
    node8 = TreeNode(8, None, node10)

    node5 = TreeNode(5, node4, node8)

    tree = BinaryTree(node5)
    assert tree.find_kth_smallest(tree.root, 2).data == 4


def test3():
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4, node2, node3)

    node7 = TreeNode(7)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node7, node10)

    node5 = TreeNode(5, node4, node8)

    tree = BinaryTree(node5)
    assert tree.find_kth_smallest(tree.root, 2).data == 4
