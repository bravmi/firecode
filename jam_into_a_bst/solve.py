from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def insert(self, root, data):
        # Return the new root
        if root is None:
            return TreeNode(data)

        if data < root.data:
            root.left_child = self.insert(root.left_child, data)
        elif data > root.data:
            root.right_child = self.insert(root.right_child, data)
        return root

    def insert_iter(self, root, data):
        # Return the new root
        new_node = TreeNode(data)
        if root is None:
            return new_node

        curr = root
        while curr:
            prev = curr
            if data < curr.data:
                curr = curr.left_child
            elif data > curr.data:
                curr = curr.right_child
            else:
                break
        if data < prev.data:
            prev.left_child = new_node
        elif data > prev.data:
            prev.right_child = new_node
        return root

    def to_list(self, root):
        if not root:
            return []

        res = []
        res.append(root.data)
        if root.left_child:
            res.extend(self.to_list(root.left_child))
        if root.right_child:
            res.extend(self.to_list(root.right_child))
        return res


if __name__ == '__main__':
    pass
