#!/usr/bin/env python
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return

    result = nums[0]

    for num in nums[1:]:
        result = result ^ num

    return result