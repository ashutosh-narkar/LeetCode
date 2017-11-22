#!/usr/bin/env python
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
(row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 <= row2 and col1 <=  col2.



Solution: Binary Indexed Tree or Fenwick Tree
Explanation about BIT: http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/


Both update and get_sum methods run in O(log m) + O(log n) time
"""


class NumMatrix:
    def __init__(self, matrix):
        if not matrix:
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self.nums = [[0] * (self.cols) for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        delta = val - self.nums[row][col]
        self.nums[row][col] = val

        # index in BITree[] is 1 more than the index in arr[]
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:

                # Add 'delta' to current node of BI Tree
                self.bit[i][j] += delta

                # Update index to that of parent
                # Parent can be obtained by removing
                # the last set bit from index, i.e., index = index - (index & (-index))
                j += (j & -j)              # WE ARE INCREMENTING THE INDEX
            i += (i & -i)                  # WE ARE INCREMENTING THE INDEX

    # to see a picture
    # https://discuss.leetcode.com/topic/29536/clean-c-solution-and-explaination-o-mn-space-with-o-1-time/2
    def sumRegion(self, row1, col1, row2, col2):
        return self.get_sum(row2, col2) + self.get_sum(row1 - 1, col1 - 1) - self.get_sum(row1 - 1, col2) - self.get_sum(row2, col1 -1)

    def get_sum(self, row, col):
        result = 0

        # index in BITree[] is 1 more than the index in arr[]
        i = row + 1

        while i > 0:
            j = col + 1
            while j > 0:

                result += self.bit[i][j]

                # Update index to that of parent. WE ARE DECREMENTING THE INDEX
                j -= (j & -j)

            # Update index to that of parent. WE ARE DECREMENTING THE INDEX
            i -= (i & -i)

        return result

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    bit = NumMatrix(matrix)
    print bit.sumRegion(2, 1, 4, 3)

    bit.update(3, 2, 2)
    print bit.sumRegion(2, 1, 4, 3)
