#!/usr/bin/env python
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


def summary_ranges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums:
        return []

    result = []

    i = 0
    while i < len(nums):
        start = i
        end = i

        while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
            end += 1

        if end > start:
            res = str(nums[start]) + "->" + str(nums[end])
            result.append(res)
        else:
            result.append(str(nums[start]))

        i = end + 1

    return result
