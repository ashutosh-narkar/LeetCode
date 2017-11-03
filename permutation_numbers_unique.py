#!/usr/bin/env python
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

Solution:

Use the same algo used for next_permutation.py and permutation_numbers.py
"""


def permute_unique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    nums.sort()

    result = list()
    result.append(nums)

    while next_permutation(nums):
        result.append(list(nums))  # make sure to create a new copy of nums

    return result


def next_permutation(nums):
    k, l = -1, -1

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            k = i

    if k == -1:
        nums.reverse()
        return False

    for i in range(k + 1, len(nums)):
        if nums[i] > nums[k]:
            l = i

    nums[k], nums[l] = nums[l], nums[k]

    nums[k + 1: len(nums): 1] = nums[len(nums) - 1: k: -1]

    return True
