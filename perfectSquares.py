#!/usr/bin/env python
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''


def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0

    # cntPerfectSquares[i] = the least number of perfect square numbers
    # which sum to i. Note that cntPerfectSquares[0] is 0.
    cntPerfectSquares = [float('inf')] * (n + 1)

    cntPerfectSquares[0] = 0

    for i in range(1, n + 1):
        # For each i, it must be the sum of some number (i - j*j) and
        # a perfect square number (j*j).

        j = 1
        while j * j <= i:
            cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j * j] + 1)
            j += 1

    return cntPerfectSquares[n]