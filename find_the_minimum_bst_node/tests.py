from .solve import *


def test1():
    node2 = TreeNode(2)
    node5 = TreeNode(5)
    node10 = TreeNode(10)
    node8 = TreeNode(8, node5, node10)
    node4 = TreeNode(4, node2, node8)

    tree = BinaryTree()
    assert tree.find_min(node4).data == 2
