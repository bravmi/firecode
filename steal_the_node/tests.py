from .solve import *


def test1():
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node5 = TreeNode(5)
    node8 = TreeNode(8, node5)
    node4 = TreeNode(4, node2, node8)

    node9 = TreeNode(9, node4)
    tree = BinaryTree(node9)
    tree.delete(tree.root, 9)
    assert tree.level_order() == [4, 2, 8, 1, 5]


def test2():
    node1 = TreeNode(1)
    tree = BinaryTree(node1)
    tree.delete(tree.root, 1)
    assert tree.level_order() is None


def test3():
    node1 = TreeNode(1)
    node5 = TreeNode(5)
    node4 = TreeNode(4, node1, node5)

    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node8 = TreeNode(8, node7, node9)

    node6 = TreeNode(6, node4, node8)
    tree = BinaryTree(node6)
    tree.delete(tree.root, 4)
    assert tree.level_order() == [6, 5, 8, 1, 7, 9]


def test4():
    node1 = TreeNode(1)
    node5 = TreeNode(5)
    node4 = TreeNode(4, node1, node5)

    node9 = TreeNode(9)
    node7 = TreeNode(7, right_child=node9)

    node6 = TreeNode(6, node4, node7)
    tree = BinaryTree(node6)
    tree.delete(tree.root, 7)
    assert tree.level_order() == [6, 4, 9, 1, 5]


def test5():
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node5 = TreeNode(5)
    node4 = TreeNode(4, right_child=node5)
    node3 = TreeNode(3, node2, node4)

    node9 = TreeNode(9, node3)
    tree = BinaryTree(node9)
    tree.delete(tree.root, 3)
    assert tree.level_order() == [9, 4, 2, 5, 1]


def test6():
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node5 = TreeNode(5)
    node8 = TreeNode(8, node5)
    node4 = TreeNode(4, node2, node8)

    node9 = TreeNode(9, node4)
    tree = BinaryTree(node9)
    tree.delete(tree.root, 4)
    assert tree.level_order() == [9, 5, 2, 8, 1]
