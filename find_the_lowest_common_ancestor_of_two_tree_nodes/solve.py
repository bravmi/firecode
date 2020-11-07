from ..utils import *


class BinaryTree:
    def __init__(self, root=None):
        # Check out Use Me section to find out Node Structure
        self.root = root

    def path(self, root, node):
        if root is None:
            return []

        if root.data == node.data:
            return [root]
        curr = self.path(root.left_child, node) or self.path(
            root.right_child, node
        )
        if curr:
            curr.append(root)
            return curr
        return []

    def findLCA(self, root, node1, node2):
        # Return type should be of type TreeNode
        path1 = self.path(root, node1)
        path2 = self.path(root, node2)
        path2 = set(path2)

        for node in path1:
            if node in path2:
                return node
        return None


if __name__ == '__main__':
    node6 = TreeNode(
        6,
        TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5)),
        TreeNode(8, None, TreeNode(9)),
    )
    tree = BinaryTree(node6)
    assert tree.findLCA(tree.root, TreeNode(3), TreeNode(4)).data == 4
