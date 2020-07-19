from functools import wraps


class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'TreeNode({self.data!r})'


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def to_list(self):
        curr = self
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'Node({self.data!r})'


class Range:
    def __init__(self, lower_bound=-1, upper_bound=-1):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'[{self.lower_bound!r},{self.upper_bound!r}]'

    def to_list(self):
        return [self.lower_bound, self.upper_bound]


def cached(func):
    cache = {}

    @wraps(func)
    def with_cache(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return with_cache
