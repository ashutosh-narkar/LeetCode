#!/usr/bin/env python
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


# Iterative Solution

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    r = list(s)
    low = 0
    high = len(r) - 1

    while low < high:
        r[low], r[high] = r[high], r[low]
        low += 1
        high -= 1

    return "".join(r)


# Recursive Solution
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    l = len(s)

    if l < 2:
        return s

    return reverseString(s[l / 2:]) + reverseString(s[:l / 2])