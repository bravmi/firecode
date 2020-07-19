from firecode.utils import *


def is_power_of_four(number):
    test = 1
    while test < number:
        test <<= 2
    return test == number


if __name__ == '__main__':
    pass
