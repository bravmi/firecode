from firecode.utils import *


def binary_search(a_list, item):
    low, high = 0, len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] < item:
            low = mid + 1
        elif a_list[mid] > item:
            high = mid - 1
        else:
            return True
    return False


if __name__ == '__main__':
    pass
