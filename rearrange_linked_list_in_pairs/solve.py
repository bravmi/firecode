from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def arrange_in_pairs(self):
        """
        O(n) time, O(n) space
        straightforward approach
        """
        arr = self.to_list()

        curr = None
        i, j = 0, len(arr) - 1
        while i < j:
            curr = Node(arr[i], curr)
            curr = Node(arr[j], curr)
            i += 1
            j -= 1
        if i == j:
            curr = Node(arr[i], curr)
        self.head = curr

        self.reverse()

    def reverse(self):
        if not self.head or not self.head.next:
            return

        prev = None
        curr = self.head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        self.head = prev

    def to_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


if __name__ == '__main__':
    node1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    l = SinglyLinkedList(node1)
    l.arrange_in_pairs()
    assert l.to_list() == [1, 5, 2, 4, 3]
