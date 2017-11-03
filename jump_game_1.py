#!/usr/bin/env python
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

'''
# @param A, a list of integers
# @return a boolean


def can_jump(A):

    if not A:
        return False

    # index reached so far
    m = 0

    for i in range(len(A)):
        if i <= m:
            # max index I can reach from i
            m = max(m, i + A[i])

            # reached end
            if m >= len(A) - 1:
                return True

    return False
