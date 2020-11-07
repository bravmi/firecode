from ..utils import *


class BinaryTree:
    """ :param max_holder: max sum path found so far """

    def __init__(self, root=None):
        self.root = root
        self.max_holder = 0

    # All the necessary collection moduled have been already imported.
    def max_sum_path(self, root):
        """ O(n) time, O(h) space
        where h is the height """
        if root is None:
            return 0

        self.max_holder = 0
        self._max_sum_path(root)
        return self.max_holder

    def _max_sum_path(self, root):
        """ Helper, returns max sum path from root to the bottom """
        if root is None:
            return 0

        left_sum = self._max_sum_path(root.left_child)
        right_sum = self._max_sum_path(root.right_child)
        self.max_holder = max(
            left_sum + root.data + right_sum, self.max_holder
        )
        return max(left_sum, right_sum) + root.data


if __name__ == '__main__':
    pass
