from ..utils import *


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end0(self, n):
        n = -n
        m = len(self)
        if not (-m <= n < 0):
            return None
        n += m

        node = self.head
        for _ in range(n):
            node = node.next
        return node

    def find_nth_node_from_end(self, n):
        shifted = self.head
        for _ in range(n):
            if shifted is None:
                return None
            shifted = shifted.next

        node = self.head
        while shifted:
            node = node.next
            shifted = shifted.next
        return node

    def __len__(self):
        return sum(1 for x in self)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next


if __name__ == '__main__':
    node6 = Node(6)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    list_ = SinglyLinkedList(node1)
    print(list_.find_nth_node_from_end(2).data)
