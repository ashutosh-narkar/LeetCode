#!/usr/bin/env python
"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

Solution:

1) find the length of the number where the nth digit is from
2) find the actual number where the nth digit is from
3) find the nth digit and return


Visualize:
1 - 9  : 9 * 1              (There are 9 numbers having 1 digit each)
10 - 99 : 90 * 2            (There are 90 numbers having 2 digits each)
100 - 999 : 900 * 3         (There are 900 numbers having 3 digits each)
1000 - 9999 : 9000 * 4      (There are 9000 numbers having 4 digits each)
"""


def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    start = 1
    len = 1
    count = 9

    while n > len * count:
        n -= len * count
        len += 1
        count *= 10
        start *= 10

    # find the actual number where the nth digit is from
    start = start + (n - 1) / len

    # identify the nth digit
    return int(str(start)[(n - 1) % len])