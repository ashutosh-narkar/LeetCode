#!/usr/bin/env python
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

# Solution is same like finding the starting point of a linked list cycle

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return -1

    slow, fast = 0, 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    find = 0
    while find != slow:
        slow = nums[slow]
        find = nums[find]

    return find
