#!/usr/bin/env python
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Solution:
Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container. 
Fix the higher one and flow water from the lower part. 
For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container

'''
def trap(A):

    if not A:
        return 0

    left = 0
    right = len(A) - 1

    maxLeft, maxRight = 0, 0 
    result =0

    while left < right:

        if A[left] <= A[right]:
            if A[left] >= maxLeft:
                maxLeft = A[left]

            # store water
            else:
                result += maxLeft - A[left]

            left += 1

        else:

            if A[right] >= maxRight:
                maxRight = A[right]

            # store water
            else:
                result += maxRight - A[right]

            right -= 1

    return result



#################################################################
# Similar idea


def trap(A):

    if not A:
        return 0

    left = 0
    right = len(A) - 1

    level = 0 
    result =0

    while left < right:

        level = max(min(A[left], A[right]), level)

        if A[left] <= A[right]:
            result += level - A[left]
            left += 1

        else:
            result += level - A[right]
            right -= 1
    

    return result
