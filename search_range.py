#!/usr/bin/env python
'''
*** LOOK AT search_array_duplicates.py


Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Runtime - O(logn)
Although the bsearch is in the loop, the search only starts in the range that is either the first half or the last half left by previous bsearch. 
You can consider it as resuming the previous bsearch. Therefore, the time complexity for each while statement is O(logn).
'''


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return [-1, -1]

    idx = binarySearch(nums, 0, len(nums) - 1, target)

    if idx == -1:
        return [-1, -1]

    result = [-1, -1]

    # start  where first instance of the number found
    left, right = idx, idx

    while left != -1:
        result[0] = left
        left = binarySearch(nums, 0, left - 1, target)

    while right != -1:
        result[1] = right
        right = binarySearch(nums, right + 1, len(nums) - 1, target)

    return result


def binarySearch(nums, low, high, target):
    while low <= high:
        mid = low + (high - low) / 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            low = mid + 1

        else:
            high = mid - 1
    return -1