#!/usr/bin/env python
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
# Time : O(n)
# Space: O(n)

def twoSum(nums, target):
    if not nums:
        return []

    lookup = {}

    for idx, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target-num], idx]
        lookup[num] = idx

    return []



if __name__=='__main__':
    nums = [2, 7, 11, 15]
    print twoSum(nums, 9)
