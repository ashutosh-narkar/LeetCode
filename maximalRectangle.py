#!/usr/bin/env python
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.


Solution:
The solution is based on "largest rectangle in histogram" solution.
Every row in the matrix is viewed as the ground with some buildings on it.
The building height is the count of consecutive ones (1s) from that row to above rows.

The rest is then the same as this solution for largest rectangle in histogram
'''


def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    height, width = len(matrix), len(matrix[0])

    m = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == '1':
                m[i][j] = m[i - 1][j] + 1

    return max(largestRectangleArea(row) for row in m)


def largestRectangleArea(height):
    if not height:
        return 0

    height.append(0)
    stack = []
    max_area = 0

    for i in range(len(height)):
        if not stack or height[i] >= height[stack[-1]]:
            stack.append(i)

        else:
            while (stack and height[stack[-1]] > height[i]):
                top = stack.pop()
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, height[top] * width)

            stack.append(i)

    return max_area