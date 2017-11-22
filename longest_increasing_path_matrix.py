#!/usr/bin/env python
"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Solution:
1) Do DFS from every cell
2) Compare 4 directions and skip cells that are out of boundary or smaller
3) Maintain cache to avoid revisits. Hence Runtime: O(matrix_rows * matrix_cols)
"""


def longest_increasing_path(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    if not matrix:
        return 0

    nrows = len(matrix)
    ncols = len(matrix[0])

    dp = [[0] * ncols for _ in range(nrows)]

    max_len = 1
    for i in range(nrows):
        for j in range(ncols):
            res = dfs(matrix, i, j, dp)
            max_len = max(max_len, res)

    return max_len


def dfs(matrix, row, col, dp):
    # invalid row
    if row < 0 or row >= len(matrix):
        return

    # invalid col
    if col < 0 or col >= len(matrix[0]):
        return

    # already calculated
    if dp[row][col] != 0:
        return dp[row][col]

    # up, down, left, right
    val = matrix[row][col]
    dp[row][col] = 1 + max(
        dfs(matrix, row - 1, col, dp) if row > 0 and val < matrix[row - 1][col] else 0,
        dfs(matrix, row + 1, col, dp) if row < len(matrix) - 1 and val < matrix[row + 1][col] else 0,
        dfs(matrix, row, col - 1, dp) if col > 0 and val < matrix[row][col - 1] else 0,
        dfs(matrix, row, col + 1, dp) if col < len(matrix[0]) - 1 and val < matrix[row][col + 1] else 0
    )

    return dp[row][col]
