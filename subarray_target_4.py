#!/usr/bin/env python
'''
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2
that sums up to the multiple of k, that is, sums up to n * k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


Solution:
1) If k == 0, then search for any consecutive pair of 0s.

2) Else, we will keep track of indices of the cumulative sum mod by k in a dictionary.
We will return True if we've seen a cumulative sum % k at least 2 indices before.

This means that there is a subarray that has a sum(subarray) % k == 0 and that subarray contains at least 2 elements.
'''
def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:
        return False

    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True

        return False

    d = {}
    d[0] = -1

    runningSum = 0

    for i in range(len(nums)):
        runningSum = (runningSum + nums[i]) % k
        if runningSum in d and i - d[runningSum] > 1:
            return True

        if runningSum not in d:
            d[runningSum] = i

    return False