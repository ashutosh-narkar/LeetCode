#!/usr/bin/env python
"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""


def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = [1]

    while len(result) < n:
        next = result[-1] * 10

        while next > n:
            next /= 10
            next += 1

            while next % 10 == 0:  # deal with case like 199+1=200 when we need to restart from 2.
                next /= 10

        result.append(next)

    return result
