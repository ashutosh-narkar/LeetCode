#!/usr/bin/env python
"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers
given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Solution: Same as ugly_number_2.py

Runtime: O(kn). A O(logk * n) can be implemented using a heap
"""


def nth_super_ugly_number(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if not n:
        return -1

    # 1 is an ugly number
    result = [1]

    # corresponding index in the arraylist for the multiplier
    index = [0] * len(primes)

    while len(result) < n:

        # find next ugly number
        next_ugly = float('inf')

        for i in range(len(primes)):
            next_ugly = min(next_ugly, primes[i] * result[index[i]])

        # update result
        result.append(next_ugly)

        # increment the index of the multiplier used
        for i in range(len(primes)):
            while next_ugly >= primes[i] * result[index[i]]:
                index[i] += 1

    return result[-1]
