from firecode.utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_full_nodes(self, root=None):
        if root:
            self.root = root
        return self._number_of_full_nodes()

    def _number_of_full_nodes(self):
        if not self.root:
            return 0

        stack = [self.root]
        count = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            elif node.left_child and node.right_child:
                count += 1
            stack.extend([node.left_child, node.right_child])
        return count


if __name__ == '__main__':
    pass
