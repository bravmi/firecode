from ..utils import *


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def path(self, root, data):
        if root is None:
            return []

        if root.data == data:
            return [root]
        curr = self.path(root.left_child, data) or self.path(
            root.right_child, data
        )
        if curr:
            curr.append(root)
            return curr
        return []

    def get_node_distance(self, root, data1, data2):
        path1 = self.path(root, data1)
        path2 = self.path(root, data2)
        return len(set(path1) ^ set(path2))


if __name__ == '__main__':
    node6 = TreeNode(
        1,
        TreeNode(2, TreeNode(None, TreeNode(4))),
        TreeNode(3, None, TreeNode(5)),
    )
    tree = BinaryTree(node6)
    assert tree.get_node_distance(tree.root, 2, 5) == 3
