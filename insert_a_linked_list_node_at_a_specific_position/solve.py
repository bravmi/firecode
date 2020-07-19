from firecode.utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        curr = self.head
        i = 1
        while curr:
            if i == pos:
                prev.next = new_node
                new_node.next = curr
                return
            prev, curr = curr, curr.next
            i += 1
        prev.next = new_node

    def to_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


if __name__ == '__main__':
    pass
