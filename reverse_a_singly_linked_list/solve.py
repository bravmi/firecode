from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            # curr.next, prev, curr = prev, curr, curr.next
            next_ = curr.next  # save next
            curr.next = prev  # reverse pointer
            prev, curr = curr, next_  # shift forward
        self.head = prev

    def to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


if __name__ == '__main__':
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    lst = SinglyLinkedList(node1)
    lst.reverse()
    print(lst.to_list())
