import collections as co

from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper method
    def find_min(self, root):
        if not root:
            return None
        if not root.left_child:
            return root
        return self.find_min(root.left_child)

    def find_min_(self, root):
        """Returns both its parent and the minimum node itself"""
        if not root:
            return None, None

        prev, curr = None, root
        while curr.left_child:
            prev, curr = curr, curr.left_child
        return prev, curr

    def delete(self, root, data):
        # Return the new root node of type TreeNode
        self.root = self._delete(root, data)
        return self.root

    def _delete(self, root, data):
        if not root:
            return None

        if data == root.data:
            if root.left_child and root.right_child:
                psucc, succ = self.find_min_(root.right_child)
                # cut the successor
                if psucc:
                    psucc.left_child = succ.right_child
                else:  # the parent is root then
                    root.right_child = succ.right_child
                # paste it in place of the root
                succ.left_child = root.left_child
                succ.right_child = root.right_child
                return succ

            elif root.left_child:
                return root.left_child
            elif root.right_child:
                return root.right_child
            else:
                return None

        elif data < root.data:
            root.left_child = self._delete(root.left_child, data)
        elif data > root.data:
            root.right_child = self._delete(root.right_child, data)
        return root

    def level_order(self):
        if self.root is None:
            return None

        acc = []
        queue = co.deque([self.root])
        while queue:
            node = queue.pop()
            if node is None:
                continue
            acc.append(node.data)
            queue.appendleft(node.left_child)
            queue.appendleft(node.right_child)
        return acc


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node5 = TreeNode(5)
    node8 = TreeNode(8, node5)
    node4 = TreeNode(4, node2, node8)

    node9 = TreeNode(9, node4)
    tree = BinaryTree(node9)
    tree.delete(tree.root, 4)
    assert tree.level_order() == [9, 5, 2, 8, 1]
