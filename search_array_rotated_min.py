#!/usr/bin/env python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
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
        mid = low + (high - low) / 2

        # if the element before the 'mid' is more than it, then nums[mid] is the minimum
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]

        # if the leftmost element is smaller than nums[mid] and nums[mid] is
        # greater than the rightmost element, the minimum value can be between
        # 'mid' and 'high'. This is because, the array is increasing from low to mid.
        elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
            low = mid + 1

        else:
            high = mid - 1

    # NOT RETURNING -1
    return nums[low]