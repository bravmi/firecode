from .solve import *


def test1():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node1.left_child = node2
    node1.right_child = node3
    node2.left_child = node4
    node2.right_child = node5
    node3.left_child = node6
    node3.right_child = node7
    node4.left_child = node8
    node4.right_child = node9

    tree = BinaryTree(node1)
    assert tree.number_of_leaves(tree.root) == 5
