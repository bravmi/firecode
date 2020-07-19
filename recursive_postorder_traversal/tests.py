from .solve import *


def test1():
    post_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.right_child = BinaryTree('c')
    tree.postorder()
    assert post_ordered_list == ['b', 'c', 'a']


def test2():
    post_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.left_child.left_child = BinaryTree('d')
    tree.left_child.right_child = BinaryTree('e')
    tree.right_child = BinaryTree('c')
    tree.postorder()
    assert post_ordered_list == ['d', 'e', 'b', 'c', 'a']


def test3():
    post_ordered_list.clear()
    tree = BinaryTree('a')
    tree.postorder()
    assert post_ordered_list == ['a']


def test4():
    post_ordered_list.clear()
    tree = BinaryTree('a')
    tree.left_child = BinaryTree('b')
    tree.postorder()
    assert post_ordered_list == ['b', 'a']
