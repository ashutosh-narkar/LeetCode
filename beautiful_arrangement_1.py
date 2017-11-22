#!/usr/bin/env python
"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is
constructed by these N numbers successfully if one of the following is true
for the ith position (1 <= i <= N) in this array:

1) The number at the ith position is divisible by i.
2) i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:
N is a positive integer and will not exceed 15.
"""


def count_arrangement(N):
    """
    :type N: int
    :rtype: int
    """
    if not N:
        return 0

    used = [0] * (N + 1)
    result = [0]

    backtrack(N, 1, used, result)
    return result[0]


def backtrack(N, pos, used, result):
    if pos > N:
        result[0] += 1
        return

    for i in range(1, N + 1):
        if used[i] == 0 and (i % pos == 0 or pos % i == 0):
            used[i] = 1
            backtrack(N, pos + 1, used, result)
            used[i] = 0
