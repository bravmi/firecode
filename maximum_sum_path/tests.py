from .solve import *


def test1():
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3 = TreeNode(3, node6, node7)

    node1 = TreeNode(1, node2, node3)
    tree = BinaryTree(node1)
    assert tree.max_sum_path(tree.root) == 18


def test2():
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1 = TreeNode(1, node2, node3)
    tree = BinaryTree(node1)
    assert tree.max_sum_path(tree.root) == 6


def test3():
    node4 = TreeNode(4)
    node2 = TreeNode(2, node4)

    node6 = TreeNode(6)
    node3 = TreeNode(3, node6)

    node1 = TreeNode(1, node2, node3)
    tree = BinaryTree(node1)
    assert tree.max_sum_path(tree.root) == 16


def test4():
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node4 = TreeNode(4, node8, node9)

    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3 = TreeNode(3, node6, node7)

    node1 = TreeNode(1, node2, node3)
    tree = BinaryTree(node1)
    assert tree.max_sum_path(tree.root) == 26


def test5():
    node1 = TreeNode(1, TreeNode(2, TreeNode(10), TreeNode(10)), TreeNode(3))
    tree = BinaryTree(node1)
    assert tree.max_sum_path(tree.root) == 22
