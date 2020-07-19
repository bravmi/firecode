from firecode.utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
        self.sizes = {None: 0}

    # Helper Method
    def size(self, root):
        if root is None:
            return 0
        if root not in self.sizes:
            self.sizes[root] = (
                self.size(root.left_child) + 1 + self.size(root.right_child)
            )
        return self.sizes[root]

    def find_kth_largest(self, root, k):
        # Return Element should be of type TreeNode
        if not root:
            return TreeNode(None)

        right_size = self.size(root.right_child)
        if right_size + 1 == k:
            return root
        elif right_size + 1 < k:
            return self.find_kth_largest(root.left_child, k - right_size - 1)
        elif right_size + 1 > k:
            return self.find_kth_largest(root.right_child, k)
        return None


if __name__ == '__main__':
    pass
