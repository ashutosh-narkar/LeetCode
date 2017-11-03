#!/usr/bin/env python
'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0  <= N <= 500.
All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


Solution:
1) Iterate the first 2 lists and maintain the Sum Count ie number of times sum is seen
2) Iterate the other 2 list and find a sum that is negative of the current sum.
3) If such a sum exists in the dict, then we have found a pair !

'''


def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    sumCount = {}
    count = 0

    for num1 in A:
        for num2 in B:
            sum = num1 + num2
            if sum in sumCount:
                sumCount[sum] += 1
            else:
                sumCount[sum] = 1

    for num1 in C:
        for num2 in D:
            target = -(num1 + num2)

            if target in sumCount:
                count += sumCount[target]

    return count
