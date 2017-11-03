#!/usr/bin/env python
"""
Given an integer array, your task is to find ALL the different possible increasing subsequences
of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain DUPLICATES, and two equal integers should also be considered
as a special case of increasing sequence.


Solution: Backtracking

** LOOK AT HOW DUPLICATES IN THE RESULT ARE HANDLED **
"""


def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    result = set()     # NOT a list like we normally do
    temp = []

    backtrack(result, temp, nums, 0)
    return list(result)   # convert result to a list


def backtrack(result, temp, nums, start):
    if len(temp) >= 2:
        result.add(tuple(temp))    # TEMP is converted to a TUPLE and not as list as list can't be added to a set

    for i in range(start, len(nums)):
        if not temp or temp[-1] <= nums[i]:
            temp.append(nums[i])
            backtrack(result, temp, nums, i + 1)
            temp.pop()