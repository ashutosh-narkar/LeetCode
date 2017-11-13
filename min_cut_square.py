#!/usr/bin/env python
"""
**** NOT YET PROPERLY WORKING *****
http://www.geeksforgeeks.org/paper-cut-minimum-number-squares-set-2/
https://ideone.com/HbiFOH

Given a paper of size A x B. Task is to cut the paper into squares of any size.
Find the minimum number of squares that can be cut from the paper.

Examples:

Input  : 36 x 30
Output : 5
Explanation :
3 (squares of size 12x12) +
2 (squares of size 18x18)

Input  : 4 x 5
Output : 5
Explanation :
1 (squares of size 4x4) +
4 (squares of size 1x1)

Solution:
Assuming we have a rectangle with width is N and height is M.

1) if (N == M), so it is a square and nothing need to be done.

2) Otherwise, we can divide the rectangle into two other smaller one (N - x, M) and (x, M),
so it can be solved recursively.

3) Similarly, we can also divide it into (N, M - x) and (N, x)

"""


def min_square(m, n):
    if m == n:
        return 1

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    helper(m, n, dp)

    return dp[m][n]


def helper(m, n, dp):

    # Initializing max values to vertical_min
    # and horizontal_min
    vertical_min = float('inf')
    horizontal_min = float('inf')

    # If the given rectangle is already a square
    if m == n:
        return 1

    # If the answer for the given rectangle is
    # previously calculated return that answer
    if dp[m][n] != 0:
        return dp[m][n]

    # The rectangle is cut horizontally and
    # vertically into two parts and the cut
    # with minimum value is found for every
    # recursive call.

    # Horizontal cut
    for i in range(1, m/2):
        horizontal_min = min(horizontal_min, helper(i, n, dp) + helper(m - i, n, dp))

    # Vertical cut
    for j in range(1, n/2):
        vertical_min = min(vertical_min, helper(m, j, dp) + helper(m, n - j, dp))

    # Minimum of the vertical cut or horizontal
    # cut to form a square is the answer
    dp[m][n] = min(vertical_min, horizontal_min)

    return dp[m][n]

if __name__ == '__main__':
    m = 4
    n = 5

    print min_square(m, n)