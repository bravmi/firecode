from .solve import *


def test9():
    node9 = TreeNode(9)
    node8 = TreeNode(8)
    node4 = TreeNode(4, node8, node9)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3 = TreeNode(3, node6, node7)
    node1 = TreeNode(1, node2, node3)

    tree = BinaryTree(node1)
    assert tree.number_of_full_nodes(tree.root) == 4


def test1():
    node1 = TreeNode(1)

    tree = BinaryTree(node1)
    assert tree.number_of_full_nodes(tree.root) == 0
