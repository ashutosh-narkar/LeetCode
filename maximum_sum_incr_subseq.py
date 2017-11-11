#!/usr/bin/env python
"""
Given an array of n positive integers.
Write a program to find the sum of maximum sum subsequence of the given array such that the integers
in the subsequence are sorted in increasing order.

Example 1: Input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100),
Example 2: Input is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10)
Example 3: Input is {10, 5, 4, 3}, then output should be 10

Recurrence Relation: If the current number(index i) is greater than the previous numbers(index j)
and if dp[i] < dp[j] + nums[i] then update dp[i]
"""

def max_sum_IS(nums):
    if not nums:
        return 0

    maxSum = 0

    # dp[i] be the max sum of the increasing subsequence till index 'i' in nums
    dp = [0] * len(nums)

    # for each number the sum is atleast the number itself
    for i in range(len(dp)):
        dp[i] = nums[i]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]

    # find the max
    for item in dp:
        if item > maxSum:
            maxSum = item

    return maxSum


if __name__ == '__main__':
    input = [1,101, 2, 3, 100, 4, 5]
    print max_sum_IS(input)

    input = [3, 4, 5, 10]
    print max_sum_IS(input)

    input = [10, 5, 4, 3]
    print max_sum_IS(input)