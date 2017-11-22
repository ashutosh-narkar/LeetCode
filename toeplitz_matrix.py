#!/usr/bin/env python
"""
Given a square matrix, find if it's a Toeplitz matrix or not.
A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant,
i.e., all elements in a diagonal are same.

Input: mat[N][N] = {{ 6, 7, 8},
                    { 4, 6, 7},
                    { 1, 4, 6}},
Output : True;
Values in all diagonals are same.

Input: mat[N][N] = {{ 6, 7, 8, 9 },
                    { 4, 6, 7, 8 },
                    { 1, 4, 6, 7 },
                    { 0, 1, 4, 6 },
                    { 2, 0, 1, 4 }};
Output : True;

Input: mat[N][N] = {{ 6, 3, 8},
                    { 4, 9, 7},
                    { 1, 4, 6}},
Output : False

Solution: Check if an element at (i, j) is same as its immediate diagonal at (i + 1, j + 1)
"""


def is_toeplitz(matrix):
    if not matrix:
        return False

    nrows = len(matrix)
    ncols = len(matrix[0])

    for i in range(nrows - 1):
        for j in range(ncols - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False

    return True

if __name__ == '__main__':
    matrix = [[6, 7, 8],
              [4, 6, 7],
              [1, 4, 6]]

    print is_toeplitz(matrix)

    matrix = [[6, 7, 8, 9],
              [4, 6, 7, 8],
              [1, 4, 6, 7],
              [0, 1, 4, 6],
              [2, 0, 1, 4]]

    print is_toeplitz(matrix)

    matrix = [[6, 3, 8],
              [4, 9, 7],
              [1, 4, 6]]
    print is_toeplitz(matrix)
