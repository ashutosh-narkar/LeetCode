#!/usr/bin/env python
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
'''

def spiralOrder(matrix):

    if not matrix:
        return []

    if len(matrix) == 1:
        return matrix[0]

    result = []
  
    nrows = len(matrix)
    ncols = len(matrix[0])

    top = 0
    bottom = nrows - 1

    left = 0
    right = ncols - 1


    while (left <= right and top <= bottom):
   
        # left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])

        top += 1

        # top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right]) 

        right -= 1

        # check if the bottom line hasn't been pushed
        # this condition prevents duplicate rows
        if bottom >= top:
            # right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])

            bottom -= 1


        # check if the left line haven't been pushed
        # this condition prevents duplicate columns
        if left <= right:
            # bottom to top
            for i in range(bottom, top -1, -1):
                result.append(matrix[i][left])

            left += 1

    return result
    


if __name__ == '__main__':
    data = [[ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]]

    print 'Spiral ordering is {}'.format(spiralOrder(data))



