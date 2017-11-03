#!/usr/bin/env python
'''
Given a collection of numbers, return all possible unique permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

For example, [1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

Alternate Question:
Given a deck of card, shuffle them so that any permutation is equally likely.
'''


# Solution 1: Using next permutation
def permute(nums):
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
        result.append(list(nums))     # make sure to create a new copy of nums

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




# See general Backtracking template at
# https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning
# Solution 2: Backtracking.
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    result = []
    temp = []
    backtrack(result, temp, nums)
    return result


def backtrack(result, temp, nums):
    if len(temp) == len(nums):
        result.append(list(temp))  # make deep copy or it gets overwritten

    else:
        for num in nums:
            if num in temp:
                continue      # element already exists, skip

            temp.append(num)
            backtrack(result, temp, nums)
            temp.pop()








# Solution 2: Don't Use
import sys

def permutations(nums):
    if len(nums) <= 1:
        return [nums]  # since we want a result as a list of lists

    perms = permutations(nums[1:]) 
    num = nums[0]
    
    result = []

    for perm in perms:
        for i in range(len(perm) + 1):
            res = list(perm)
            res.insert(i, num)
            result.append(res)
    return result
    


