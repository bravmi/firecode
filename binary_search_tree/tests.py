from .solve import *


def test1():
    node5 = TreeNode(5)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node5, node10)

    node2 = TreeNode(2)
    node4 = TreeNode(4, node2, node8)

    tree = BinaryTree(node4)
    assert tree.find_max(tree.root).data == 10


def test2():
    tree = BinaryTree()
    assert tree.find_max(None) is None
