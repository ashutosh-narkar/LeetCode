#!/usr/bin/env python
'''
Given an array of integers and an integer k, you need to
find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

# Solution 1: Time complexity : O(n)  Space complexity : O(n)
# Maintain a dict of form {sum, occurrence of sum}

def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0

    count = 0
    accumulated_sum = 0

    d = {}
    d[0] = 1

    for num in nums:
        accumulated_sum += num
        if (accumulated_sum - k) in d:
            count += d[accumulated_sum - k]

        if accumulated_sum not in d:
            d[accumulated_sum] = 1
        else:
            d[accumulated_sum] += 1

    return count



# Solution 2: We can choose a particular start point and while iterating over the end points,
# we can add the element corresponding to the end point to the sum formed till now.
# Whenever the sum equals the required k value, we can update the count value.
# We do so while iterating over all the end indices possible for every start index.
# Whenever, we update the start index, we need to reset the sum value to 0.

# Time complexity : O(n^2)  Space complexity : O(1)

def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0

    count = 0

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == k:
                count += 1

    return count
