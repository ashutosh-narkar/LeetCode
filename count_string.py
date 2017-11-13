#!/usr/bin/env python
"""
Given a length n, count the number of strings of length n that can be made using 'a', 'b' and 'c'
with at-most one 'b' and two 'c's allowed.

Example:

Input : n = 3
Output : 19
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb

Input  : n = 4
Output : 39
"""


def count_str(n):

    b_count = 1
    c_count = 2
    dp = [[[-1] * (c_count + 1)] * (b_count + 1) for _ in range(n + 1)]

    helper(n, dp, b_count, c_count)
    return dp[n][b_count][c_count]


def helper(n, dp, b_count, c_count):

    # base cases
    if b_count < 0 or c_count < 0:
        return 0

    if n == 0:
        return 1

    if b_count == 0 and c_count == 0:
        return 1

    # if result already cached
    if dp[n][b_count][c_count] != -1:
        return dp[n][b_count][c_count]

    # Three cases, we choose, a or b or c
    # In all three cases n decreases by 1.
    temp = helper(n - 1, dp, b_count, c_count)
    temp += helper(n - 1, dp, b_count - 1, c_count)
    temp += helper(n - 1, dp, b_count, c_count - 1)

    dp[n][b_count][c_count] = temp

    return dp[n][b_count][c_count]

if __name__ == '__main__':
    print count_str(3)