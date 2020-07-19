from .solve import *


def test1():
    node1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    tree = BinaryTree(node1)
    assert tree.findLCA(tree.root, TreeNode(6), TreeNode(4)).data == 1


def test2():
    node6 = TreeNode(
        6,
        TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5)),
        TreeNode(8, None, TreeNode(9)),
    )
    tree = BinaryTree(node6)
    assert tree.findLCA(tree.root, TreeNode(3), TreeNode(4)).data == 4


def test3():
    node1 = TreeNode(1)
    tree = BinaryTree(node1)
    assert tree.findLCA(tree.root, node1, node1).data == 1


def test4():
    node1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    tree = BinaryTree(node1)
    assert tree.findLCA(tree.root, TreeNode(4), TreeNode(5)).data == 2


def test5():
    node1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree = BinaryTree(node1)
    assert tree.findLCA(tree.root, TreeNode(2), TreeNode(3)).data == 1


def test6():
    tree = BinaryTree()
    assert tree.findLCA(tree.root, TreeNode(1), TreeNode(1)) is None
