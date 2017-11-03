#!/usr/bin/env python
"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:
        return False

    numIndex = {}

    for i, num in enumerate(nums):
        if num in numIndex:
            diff = abs(i - numIndex[num])
            if diff <= k:
                return True

        numIndex[num] = i

    return False
