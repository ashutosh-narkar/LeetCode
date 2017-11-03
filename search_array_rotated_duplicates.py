#!/usr/bin/env python
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

When duplicates are allowed in the array, the worst case is O(n).
This is because we cannot decide where to move in the find_pivot method if nums[low] == nums[mid].
In this case, we move low pointer one step to the right and repeat
The rest conditions are always O(log n).

For example:

input: 113111111111, Looking for target 3.
'''


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    if not nums:
        return False

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) / 2

        if nums[mid] == target:
            return True

        # everything from low to mid is sorted
        elif nums[low] < nums[mid]:
            if nums[low] <= target and target < nums[mid]:  # target cannot be = mid
                high = mid - 1
            else:
                low = mid + 1

        # everything from mid to high is sorted
        elif nums[low] > nums[mid]:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        else:
            low += 1

    return False