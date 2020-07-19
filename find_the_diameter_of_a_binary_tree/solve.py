from firecode.utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node
        self.heights = {}

    def height(self, root):
        if not root:
            return 0

        if root not in self.heights:
            self.heights[root] = 1 + max(
                self.height(root.left_child), self.height(root.right_child)
            )
        return self.heights[root]

    def diameter(self, root):
        if not root:
            return 0

        ans = max(
            self.diameter(root.left_child),
            self.diameter(root.right_child),
            1 + self.height(root.left_child) + self.height(root.right_child),
        )
        return ans


if __name__ == '__main__':
    pass
