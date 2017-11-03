#!/usr/bin/env python
"""
LOOK AT remove_duplicates_array_2.py

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

def removeDuplicates(A):

    if not A:
        return 0

    if len(A) < 2:
        return len(A)

    p = 0 # position of last unique element

    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            p += 1
        A[p] = A[i]

    return p + 1   # since we have 0 indexing
