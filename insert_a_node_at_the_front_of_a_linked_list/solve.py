from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        new_node = Node()
        new_node.data = data
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


if __name__ == '__main__':
    pass
