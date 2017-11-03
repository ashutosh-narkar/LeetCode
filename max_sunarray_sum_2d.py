#!/usr/bin/env python
'''
Given a 2D array, find the maximum sum subarray in it.

http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
Runtime - O(n^3)
'''

def maxSubArray(matrix):
    if not matrix:
        return 0

    nrows = len(matrix)
    ncols = len(matrix[0])

    max_sum = float('-inf')
    start_row, start_col, end_row, end_col = [None] * 4


    for i in range(ncols):
        temp = [0] * nrows           # DO NOT initialize after next loop
        for j in range(i, ncols):
            for k in range(nrows):
                temp[k] += matrix[k][j]


            curr_sum, row1, row2 = kadane(temp)

            if curr_sum > max_sum:
                max_sum = curr_sum
                start_row = row1
                start_col = i
                end_row = row2
                end_col = j



    return (max_sum, start_row, start_col, end_row, end_col)


def kadane(nums):

    current_max = nums[0]
    overall_max = nums[0]


    start, end = 0, 0

    for i in range(1, len(nums)):

        if current_max >= 0:
            current_max += nums[i]

        else:
            current_max = nums[i]
            start = i

        if current_max > overall_max:
            overall_max = current_max
            end = i


    return (overall_max, start, end)


if __name__ == '__main__':
    input = [[1, 2, -1, -4, -20],
             [-8, -3, 4, 2, 1],
             [3, 8, 10, 1, 3],
             [-4, -1, 1, 7, -6]]

    print maxSubArray(input)













            


            
