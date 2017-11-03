#!/usr/bin/env python

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.


'''

# Solution 1: Math

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    n = len(nums)

    # Sum of 1st n integers
    expectedSum = n * (n + 1) * 0.5

    for num in nums:
        expectedSum -= num

    return int(expectedSum)


# Solution 2: But Manipulation

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    res = 0

    for i in range(len(nums)):
        res ^= (i + 1)
        res ^= nums[i]

    return res