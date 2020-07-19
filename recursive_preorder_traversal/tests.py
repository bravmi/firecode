from .solve import *


def test1():
    pre_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.left_child.left_child = BinaryTree('d')
    tree.left_child.right_child = BinaryTree('e')
    tree.right_child = BinaryTree('c')
    tree.preorder()
    assert pre_ordered_list == ['a', 'b', 'd', 'e', 'c']


def test2():
    pre_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.right_child = BinaryTree('c')
    tree.preorder()
    assert pre_ordered_list == ['a', 'b', 'c']


def test3():
    pre_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.preorder()
    assert pre_ordered_list == ['a', 'b']


def test4():
    pre_ordered_list.clear()
    tree = BinaryTree('a')
    tree.preorder()
    assert pre_ordered_list == ['a']
