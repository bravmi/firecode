from .solve import *


def test1():
    tree4 = BinaryTree(4)
    tree5 = BinaryTree(5)
    tree2 = BinaryTree(2, tree4, tree5)

    tree6 = BinaryTree(6)
    tree7 = BinaryTree(7)
    tree3 = BinaryTree(3, tree6, tree7)

    tree1 = BinaryTree(1, tree2, tree3)
    assert tree1.inorder_iterative() == [4, 2, 5, 1, 6, 3, 7]


def test2():
    tree_b = BinaryTree('b')
    tree_c = BinaryTree('c')
    tree_a = BinaryTree('a', tree_b, tree_c)
    assert tree_a.inorder_iterative() == ['b', 'a', 'c']


def test3():
    tree_d = BinaryTree('d')
    tree_e = BinaryTree('e')
    tree_b = BinaryTree('b', tree_d, tree_e)
    tree_c = BinaryTree('c')
    tree_a = BinaryTree('a', tree_b, tree_c)
    assert tree_a.inorder_iterative() == ['d', 'b', 'e', 'a', 'c']


def test4():
    tree_a = BinaryTree('a')
    assert tree_a.inorder_iterative() == ['a']


def test5():
    tree_b = BinaryTree('b')
    tree_a = BinaryTree('a', tree_b)
    assert tree_a.inorder_iterative() == ['b', 'a']
