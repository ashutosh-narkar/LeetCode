#!/usr/bin/env python
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4

Logic:
Top, Left, and Top Left decides the size of the square. If all of them are same, then the size of square increases by 1

For a picture of the dp array look at https://discuss.leetcode.com/topic/20801/extremely-simple-java-solution/2
'''


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    nrows = len(matrix)
    ncols = len(matrix[0])
    result = 0

    # dp[i,j] represents a square whose lower right corner is at (i, j)
    dp = [[0] * (ncols + 1) for _ in range(nrows + 1)]

    for i in range(1, nrows + 1):
        for j in range(1, ncols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
                result = max(dp[i][j], result)

    return result * result