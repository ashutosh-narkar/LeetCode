#!/usr/bin/env python
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''


def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    dist = 0
    n = x ^ y

    while n:
        dist += 1
        n &= (n - 1)  # n =  n & (n - 1)

    return dist
