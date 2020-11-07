from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_min(self, root):
        # Return element should be of type TreeNode
        if not root:
            return None
        if not root.left_child:
            return root

        return self.find_min(root.left_child)


if __name__ == '__main__':
    pass
