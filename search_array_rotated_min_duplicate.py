#!/usr/bin/env python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

Time Complexity : O(n). Since when there is match between nums[mid] and nums[high]
we don't know whether to go left or right

"""


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    low = 0
    high = len(nums) - 1

    while low <= high:

        while low < high and nums[low] == nums[low + 1]:
            low += 1

        while high > low and nums[high] == nums[high - 1]:
            high -= 1

        if low == high:
            return nums[low]

        mid = low + (high - low) / 2

        if nums[mid] > nums[high]:
            low = mid + 1

        else:
            high = mid

    return nums[low]