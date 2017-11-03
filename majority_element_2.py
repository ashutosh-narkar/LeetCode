#!/usr/bin/env python
"""
Given an integer array of size n, find all elements that appear more than [ n/3 ] times.
The algorithm should run in linear time and in O(1) space.

Solution: Moore voting algorithm
"""


def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []

    candidate1 = 0
    candidate2 = 1

    count1 = 0
    count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1

        elif num == candidate2:
            count2 += 1

        elif count1 == 0:
            candidate1 = num
            count1 = 1

        elif count2 == 0:
            candidate2 = num
            count2 = 1

        else:
            count1 -= 1
            count2 -= 1

    result = []

    for num in (candidate1, candidate2):
        if nums.count(num) > len(nums) / 3:
            result.append(num)

    return result
