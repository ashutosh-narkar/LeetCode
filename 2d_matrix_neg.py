#!/usr/bin/env python
'''
2D Matrix(n * n) of positive and negative numbers is given.
Matrix is sorted rowwise and columnwise.
You have to return the count of -ve numbers in most optimal way.
'''

def find_smallest_positive(numbers):
    '''
    Return the index (row, col) of the
    smallest positive number
    '''

    if not numbers:
        return -1

    row = 0
    col = len(numbers[0]) - 1

    while(row <= len(numbers) and col >= 0):
        if numbers[row][col] >= 0 and numbers[row][col-1] < 0:
            return(row, col) 

        elif numbers[row][col] < 0 and numbers[]
