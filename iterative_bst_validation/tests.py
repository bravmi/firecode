from .solve import *


def test1():
    node14 = TreeNode(14)
    node18 = TreeNode(18)
    node15 = TreeNode(15, node14, node18)

    node30 = TreeNode(30)
    node20 = TreeNode(20, node15, node30)

    tree = BinaryTree(node20)
    assert tree.validate_BST_Itr(tree.root) == True


def test2():
    node14 = TreeNode(14)
    node18 = TreeNode(18)
    node30 = TreeNode(30, node14, node18)

    node15 = TreeNode(15)
    node20 = TreeNode(20, node30, node15)

    tree = BinaryTree(node20)
    assert tree.validate_BST_Itr(tree.root) == False


def test3():
    node10 = TreeNode(10)
    node30 = TreeNode(30)
    node15 = TreeNode(15, node10, node30)

    node40 = TreeNode(40)
    node20 = TreeNode(20, node15, node40)

    tree = BinaryTree(node20)
    assert tree.validate_BST_Itr(tree.root) == False
