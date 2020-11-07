from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_max(self, root):
        # Return element should be of type TreeNode
        if not root:
            return None
        if not root.right_child:
            return root

        return self.find_max(root.right_child)


if __name__ == '__main__':
    pass
