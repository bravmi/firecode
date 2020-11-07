from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper Method
    @cached
    def size(self, root):
        if not root:
            return 0

        return self.size(root.left_child) + 1 + self.size(root.right_child)

    def find_kth_smallest(self, root, k):
        # Return element should be of Type TreeNode
        if not root:
            return TreeNode(None)

        left_size = self.size(root.left_child)
        if left_size + 1 == k:
            return root
        elif left_size + 1 > k:
            return self.find_kth_smallest(root.left_child, k)
        else:
            return self.find_kth_smallest(root.right_child, k - left_size - 1)


if __name__ == '__main__':
    pass
