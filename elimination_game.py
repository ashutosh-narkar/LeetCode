#!/usr/bin/env python
"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other
number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number
and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

Solution: Idea is to update and record head in each turn. when the total number becomes 1, head is the only number left.

When will head be updated?

1. if we move from left
2. if we move from right and the total remaining number % 2 == 1
like 2 4 6 8 10, we move from 10, we will take out 10, 6 and 2, head is deleted and move to 4
like 2 4 6 8 10 12, we move from 12, we will take out 12, 8, 4, head is still remaining 2

then we find a rule to update our head.


This is a variation of the Josephus problem.
"""


def last_remaining(n):
    """
    :type n: int
    :rtype: int
    """

    if not n:
        return -1

    left_to_right = True
    head = 1
    step = 1
    remaining = n

    while remaining > 1:
        if left_to_right or remaining % 2 == 1:
            head = head + step

        remaining /= 2
        step = 2 * step
        left_to_right = not left_to_right

    return head
