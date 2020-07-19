import math

from firecode.utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def count(self):
        n = 0
        curr = self.head
        while curr:
            curr = curr.next
            n += 1
        return n

    def find_middle_node(self):
        n = self.count()
        mid = int(math.ceil(n / 2.0))
        curr = self.head
        for _ in range(2, mid + 1):
            curr = curr.next
        return curr


if __name__ == '__main__':
    pass
