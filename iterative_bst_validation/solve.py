from sys import maxsize as INF

from firecode.utils import *


# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_Itr(self, root):
        # Return type should be Boolean
        if root is None:
            return True

        class NodeBoundary:
            def __init__(self, node, left_boundary=-INF, right_boundary=INF):
                self.node = node
                self.left_boundary = left_boundary
                self.right_boundary = right_boundary

        stack = [NodeBoundary(root)]
        while stack:
            node_boundary = stack.pop()
            if (
                node_boundary.node.data < node_boundary.left_boundary
                or node_boundary.node.data > node_boundary.right_boundary
            ):
                return False

            if node_boundary.node.left_child:
                stack.append(
                    NodeBoundary(
                        node_boundary.node.left_child,
                        node_boundary.left_boundary,
                        node_boundary.node.data,
                    )
                )
            if node_boundary.node.right_child:
                stack.append(
                    NodeBoundary(
                        node_boundary.node.right_child,
                        node_boundary.node.data,
                        node_boundary.right_boundary,
                    )
                )
        return True


if __name__ == '__main__':
    pass
