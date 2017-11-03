#!/usr/bin/env python
'''
Given a cost matrix cost[][] and a position (m, n) in cost[][],
write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).

Each cell of the matrix represents a cost to traverse through that cell.
Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).

You can only traverse down, right and diagonally lower cells from a given cell.
You may assume that all costs are positive integers.

'''
def minCost(matrix, row, col):
    if not matrix:
        return 0

    nrows = len(matrix)
    ncols = len(matrix[0])

    dp = [[0] * ncols for i in range(nrows)]

    # cost of origin
    dp[0][0] = matrix[0][0]

    # cost of first row
    for i in range(1, col + 1):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]

    # cost of first col
    for i in range(1, row + 1):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # we loop till "row + 1" and "col + 1"
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] = matrix[i][j] + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[row][col]


if __name__ == '__main__':
    input  = [[1, 2, 3],
              [4, 8, 2],
              [1, 5, 3]]

    print 'Min cost is {}'.format(minCost(input, 2, 2))
