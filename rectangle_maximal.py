#!/usr/bin/env python
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Solution:
This question is similar as [Largest Rectangle in Histogram]:

You can maintain a row length of Integer array H recorded its height of '1's, and scan and update row by row to find out the largest rectangle of each row.

For each row, if matrix[row][i] == '1'. H[i] +=1, or reset the H[i] to zero. and according the algorithm of [Largest Rectangle in Histogram], to update the maximum area.
'''
def maximalRectangle(matrix):
    if not matrix:
        return 0


    nrows = len(matrix)
    ncols = len(matrix[0])

    max_area = 0

    height = [0] * (ncols + 1) # array length is ncols + 1 since we have to add a '0' in the end, similar to Largest Rectangle in Histogram


    for i in range(nrows):
        stack = []
        for j in range(ncols + 1):
            if j < ncols:
                if matrix[i][j] == '1':
                    height[j] += 1

                else:
                    height[j] = 0

            # same logic as Largest Rectangle in Histogram        
            if not stack or height[j] >= height[stack[-1]]:
                stack.append(j)

            else:
                while stack and height[stack[-1]] > height[j]:
                    top = stack.pop()
                    width = j if not stack else j -1 - stack[-1] 
                    max_area = max(max_area, height[top] * width)

                stack.append(j)


    return max_area
