#!/usr/bin/env python
'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Recurrence:
A[i][j] = min(A[i-1][j], A[i][j-1]) +grid[i][j] 

ie. a[i][j] = value of grid + min(sum coming from rigth, sum coming from top)

**********This is same as "cost_path_matrix.py"***********
Use that method

'''
def minPathSum(grid):

    if not grid:
	return 0


    a = []
    nrows, ncols = len(grid), len(grid[0])

    # initialize
    a = [[float('inf')] * (ncols + 1) for i in range(nrows + 1)]

    # at the first step (down or right), the sum is 0
    a[0][1], a[1][0] = 0, 0

    for i in range(1, nrows + 1):
	for j in range(1, ncols  +1):
	    a[i][j] = grid[i -1][j - 1] + min(a[i][j-1], a[i-1][j])



    return (a, a[nrows][ncols])

def generateNumbers(result, original):
    nrows = len(result)
    ncols = len(result[0])

    row = nrows - 1
    col = ncols - 1

    path = []

    while (row > 0 and col > 0):
        val = result[row][col]  
  
        # if coming from right
        val1 = result[row][col - 1] + original[row - 1][col - 1]

        # if coming from top
        val2 = result[row - 1][col] + original[row - 1][col - 1]
        
        # save current number
        path.append(original[row - 1][col - 1])

        if val == val1:
            col -= 1

        else:
            row -= 1
           
     
    return path


if __name__ == '__main__':
    input = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]

    result, min_sum =  minPathSum(input)
    print 'Mininum sum is {}'.format(min_sum)

    print 'Path is {}'.format(generateNumbers(result, input))






         
