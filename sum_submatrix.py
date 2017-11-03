#!/usr/bin/env python
'''
Given a matrix, calculate the sum of a sub matrix given the start and end indices of the submatrix
'''
def sumSubMatrix(matrix, start_row, start_col, end_row, end_col):

    if not matrix:
        return 0

    nrows = len(matrix)
    ncols = len(matrix[0])

    if start_row >= nrows or end_row < 0:
        return 0
    
    if start_col >= ncols or end_col < 0:
        return 0

    result = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            result += matrix[i][j]

    return result


if __name__ == '__main__':

    input = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

    # entire matrix
    print sumSubMatrix(input, 0, 0, 3, 3)
       
    # same row
    print sumSubMatrix(input, 1, 1, 1, 3)
    
    # col
    print sumSubMatrix(input, 2, 1, 3, 1)


    # range
    print sumSubMatrix(input, 1, 0, 2, 2)
