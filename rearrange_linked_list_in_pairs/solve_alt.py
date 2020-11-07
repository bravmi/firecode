from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def cut_second_half(self):
        slow = self.head
        fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        return second_head

    def arrange_in_pairs(self):
        """
        O(n) time, O(1) space
        split-reverse-merge
        """
        if not self.head or not self.head.next:
            return

        second_head = self.cut_second_half()

        l2 = SinglyLinkedList(second_head)
        l2.reverse()
        second_head = l2.head

        # merge
        node1 = self.head
        node2 = second_head
        while node2:
            # node1.next, node2.next, node1, node2
            # = node2, node1.next, node1.next, node2.next
            next1, next2 = node1.next, node2.next
            node1.next, node2.next = node2, next1
            node1, node2 = next1, next2

    def reverse(self):
        if not self.head or not self.head.next:
            return

        prev = None
        curr = self.head
        while curr:
            # curr.next, prev, curr = prev, curr, curr.next
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
