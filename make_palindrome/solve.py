from firecode.utils import *


def is_palindrome(s):
    return s == s[::-1]


def make_palindrome(s):
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            break
    return s[:i] + s[i:] + s[:i][::-1]


def make_palindrome_rec(s):
    if is_palindrome(s):
        return s
    return s[0] + make_palindrome(s[1:]) + s[0]


if __name__ == '__main__':
    pass
