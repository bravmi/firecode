from .solve import *


def test1():
    node1 = TreeNode(
        1,
        TreeNode(2, TreeNode(None, TreeNode(4))),
        TreeNode(3, None, TreeNode(5)),
    )
    tree = BinaryTree(node1)
    assert tree.get_node_distance(tree.root, 2, 5) == 3


def test2():
    node1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8))),
        TreeNode(3, TreeNode(6, TreeNode(9)), TreeNode(7, TreeNode(10))),
    )
    tree = BinaryTree(node1)
    assert tree.get_node_distance(tree.root, 1, 9) == 3
    assert tree.get_node_distance(tree.root, 8, 10) == 6


def test3():
    node1 = TreeNode(1, TreeNode(2, TreeNode(3)),)
    tree = BinaryTree(node1)
    assert tree.get_node_distance(tree.root, 3, 1) == 2


def test4():
    node1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    tree = BinaryTree(node1)
    assert tree.get_node_distance(tree.root, 4, 6) == 4
    assert tree.get_node_distance(tree.root, 2, 5) == 1
    assert tree.get_node_distance(tree.root, 2, 6) == 3


def test5():
    node1 = TreeNode(1, None, TreeNode(2))
    tree = BinaryTree(node1)
    assert tree.get_node_distance(tree.root, 1, 2) == 1
