#!/usr/bin/env python
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

"""


def nth_ugly_number(n):
    """
    :type n: int
    :rtype: int
    """
    if not n:
        return -1

    # 1 is an ugly number
    result = [1]

    # corresponding index in the arraylist for the multiplier of 2,3,and 5.
    index2, index3, index5 = 0, 0, 0

    while len(result) < n:

        # each previous ugly number when multiplied with one of the
        # multipliers will produce an ugly number
        next_ugly = min(2 * result[index2], 3 * result[index3], 5 * result[index5])

        # update the result
        result.append(next_ugly)

        # increment the index of the multiplier used
        if next_ugly == 2 * result[index2]:
            index2 += 1

        if next_ugly == 3 * result[index3]:
            index3 += 1

        if next_ugly == 5 * result[index5]:
            index5 += 1

    return result[-1]
