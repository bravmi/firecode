from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def is_list_even(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        return count % 2 == 0

    def to_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


if __name__ == '__main__':
    pass
