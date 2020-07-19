from .solve import *


def test1():
    node17 = TreeNode(17)
    node19 = TreeNode(19)
    node18 = TreeNode(18, node17, node19)
    node14 = TreeNode(14)
    node15 = TreeNode(15, node14, node18)

    node32 = TreeNode(32)
    node35 = TreeNode(35, node32)
    node30 = TreeNode(30, None, node35)

    node20 = TreeNode(20, node15, node30)

    tree = BinaryTree()
    assert tree.height(node17) == 1
    assert tree.diameter(node17) == 1

    assert tree.height(node15) == 3
    assert tree.diameter(node15) == 4

    assert tree.diameter(node30) == 3
    assert tree.diameter(node20) == 7


def test2():
    node10 = TreeNode(10)
    node15 = TreeNode(15)
    node14 = TreeNode(14, node10, node15)

    node17 = TreeNode(17)
    node19 = TreeNode(19)
    node18 = TreeNode(18, node17, node19)

    node16 = TreeNode(16, node14, node18)
    node20 = TreeNode(20, node16)

    tree = BinaryTree()
    assert tree.diameter(node20) == 5


def test3():
    node3 = TreeNode(3)
    node2 = TreeNode(2, None, node3)
    node1 = TreeNode(1, None, node2)

    tree = BinaryTree()
    assert tree.diameter(node1) == 3


def test4():
    node5 = TreeNode(5)

    tree = BinaryTree()
    assert tree.diameter(node5) == 1


def test5():
    node10 = TreeNode(10)
    node15 = TreeNode(15)
    node14 = TreeNode(14, node10, node15)

    node17 = TreeNode(17)
    node19 = TreeNode(19)
    node18 = TreeNode(18, node17, node19)

    node16 = TreeNode(16, node14, node18)
    node30 = TreeNode(30)
    node20 = TreeNode(20, node16, node30)

    tree = BinaryTree()
    assert tree.diameter(node20) == 5


def test6():
    node2 = TreeNode(2)
    node1 = TreeNode(1, node2)

    tree = BinaryTree()
    assert tree.diameter(node1) == 2


def test7():
    node10 = TreeNode(10)
    node15 = TreeNode(15)
    node14 = TreeNode(14, node10, node15)

    node17 = TreeNode(17)
    node19 = TreeNode(19)
    node18 = TreeNode(18, node17, node19)

    node16 = TreeNode(16, node14, node18)

    tree = BinaryTree()
    assert tree.diameter(node16) == 5


def test8():
    node10 = TreeNode(10)
    node15 = TreeNode(15)
    node14 = TreeNode(14, node10, node15)

    node17 = TreeNode(17)
    node19 = TreeNode(19)
    node18 = TreeNode(18, node17, node19)

    node16 = TreeNode(16, node14, node18)
    node30 = TreeNode(30)
    node37 = TreeNode(37, node30)
    node20 = TreeNode(20, node16, node37)

    tree = BinaryTree()
    assert tree.diameter(node20) == 6


def test9():
    tree = BinaryTree()
    assert tree.diameter(None) == 0
