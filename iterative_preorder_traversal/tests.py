from .solve import *


def test1():
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.left_child.left_child = BinaryTree('d')
    tree.left_child.right_child = BinaryTree('e')
    tree.right_child = BinaryTree('c')
    pre_ordered_list = tree.preorder_iterative()
    assert pre_ordered_list == ['a', 'b', 'd', 'e', 'c']


def test2():
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.right_child = BinaryTree('c')
    pre_ordered_list = tree.preorder_iterative()
    assert pre_ordered_list == ['a', 'b', 'c']


def test3():
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    pre_ordered_list = tree.preorder_iterative()
    assert pre_ordered_list == ['a', 'b']


def test4():
    tree = BinaryTree('a')
    pre_ordered_list = tree.preorder_iterative()
    assert pre_ordered_list == ['a']
