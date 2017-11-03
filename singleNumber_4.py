#!/usr/bin/env python
"""
Given a sorted array consisting of only integers where every element appears
twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Runtime: O(logn)
"""


def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    low = 0
    high = len(nums) - 1

    while low < high:

        mid = low + (high - low) / 2

        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]

        # odd index. We move right as odd-even pairs are formed to the left of mid
        elif mid % 2 == 1 and nums[mid] == nums[mid - 1]:
            low = mid + 1

        # even index. We move right as even-odd pairs are formed to the right of mid
        elif mid % 2 == 0 and nums[mid] == nums[mid + 1]:
            low = mid + 1

        else:
            high = mid - 1

    return nums[low]