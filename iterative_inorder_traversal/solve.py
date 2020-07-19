from firecode.utils import *


class BinaryTree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return '%s' % self.data

    def inorder_iterative(self):
        """ O(n) time, O(h) space
        where h is the height """
        inorder_list = []

        stack = []
        curr = self
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left_child
            if not stack:
                break

            curr = stack.pop()
            inorder_list.append(curr.data)
            curr = curr.right_child

        return inorder_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data


if __name__ == '__main__':
    tree4 = BinaryTree(4)
    tree5 = BinaryTree(5)
    tree2 = BinaryTree(2, tree4, tree5)

    tree3 = BinaryTree(3)

    tree1 = BinaryTree(1, tree2, tree3)
    print(tree1.inorder_iterative())  # [4, 2, 5, 1, 3]
