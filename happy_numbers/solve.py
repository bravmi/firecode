from firecode.utils import *


def digits(x):
    while x:
        x, r = divmod(x, 10)
        yield r


def sum_squares(x):
    return sum(d ** 2 for d in digits(x))


def is_happy_number(number):
    history = set()
    while number not in history:
        history.add(number)
        number = sum_squares(number)
    return number == 1


if __name__ == '__main__':
    n = 12
    print('is_happy_number({}) = {}'.format(n, is_happy_number(n)))
