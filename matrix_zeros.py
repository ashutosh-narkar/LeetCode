#!/usr/bin/env python
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

def setZeroes(matrix):

    if not matrix:
        return

    nrows = len(matrix)
    ncols = len(matrix[0])

    rowHasZero = False
    colHasZero = False
    

    # scan 1st row for a zero
    for i in range(ncols):
        if matrix[0][i] == 0:
            rowHasZero = True
            break


    # scan 1st col for a zero
    for i in range(nrows):
        if matrix[i][0] == 0:
            colHasZero = True
            break
        

    # scan everthing except the first row and first col
    # if zero found, set matrix[0][col] and matrix[row][0] to 0
    # we are marking the rows and cols that are going to  be 0
    for i in range(1, nrows):
        for j in range(1, ncols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

                
    # scan every element of first row except first element
    # this is because if matrix[0][0] = 0, we will make entire first col 0
    # and hence lose any non-zero element in the first col

    # if zero found, make the entire col zero
    for i in range(1, ncols):
        if matrix[0][i] == 0:
            nullifyCol(matrix, i, nrows)



    # scan every element of first col except first element
    # if zero found, make entire row zero
    for i in range(1, nrows):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i, ncols)

            
    # check if first row and first col need to be nullified
    if rowHasZero:
        nullifyRow(matrix, 0, ncols)

    if colHasZero:
        nullifyCol(matrix, 0, nrows)
        

    return

            
def nullifyCol(matrix, col, nrows):

    '''
    Nullify given column
    '''
    for i in range(nrows):
        matrix[i][col] = 0

    return


def nullifyRow(matrix, row, ncols):

    '''
    Nullify the given row
    '''

    for i in range(ncols):
        matrix[row][i] = 0

    return

       
