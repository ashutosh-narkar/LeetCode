#!/usr/bin/env python
'''
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

import sys

def generateMatrix(n):

        if n == 0:
            return []


        matrix = []
        nrows, ncols = n, n


        for i in range(n):
            row = [float('inf')] * n
            matrix.insert(i, row)

        top = 0
        bottom = nrows - 1
        
        left = 0
        right = ncols - 1

        num = 1

        while(left <= right and top <= bottom):
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1


            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

        

            if bottom >= top:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1

                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        if n % 2 != 0:
            matrix[n / 2][n / 2] = num - 1;

        return matrix

        
if __name__ == '__main__':
    n = int(sys.argv[1])
    print 'Spiral square matrix of size {} is {}'.format(n, generateMatrix(n))
