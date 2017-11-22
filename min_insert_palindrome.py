#!/usr/bin/env python
"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.

Solution:

Minimum number of insertions = Length(s) - Length_LCS(s, rev_s)
"""


def find_min_insertions(s):
    if not s:
        return 0

    length_lcs = lcs(s, s[::-1])

    return len(s) - length_lcs


def lcs(s, t):
    m = len(s)
    n = len(t)

    dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

    for i in range(n + 1):
        dp[0][i] = 0

    for i in range(m + 1):
        dp[i][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__ == '__main__':
    assert find_min_insertions('geeks') == 3
    assert find_min_insertions('ab') == 1
    assert find_min_insertions('aba') == 0
    assert find_min_insertions('abc') == 2
    assert find_min_insertions('aa') == 0
    assert find_min_insertions('abcd') == 3
    assert find_min_insertions('abcda') == 2
    assert find_min_insertions('abcde') == 4

    print 'Tests Passed'
