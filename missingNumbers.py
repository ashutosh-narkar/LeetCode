#!/usr/bin/env python
'''
Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


Solution:

For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.
'''


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    result = []
    for i, num in enumerate(nums):
        if num >= 0:
            result.append(i + 1)  # since zero-based indexing ie 0th index has 1

    return result
