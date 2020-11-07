from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def is_cyclic(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    pass
