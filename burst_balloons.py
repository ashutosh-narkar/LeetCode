#!/usr/bin/env python
"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons.

If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Solution:
We need to find a way to divide the problems.

If we start from the first balloon, we can't determine the left/right for the number in each sub-problem.
Hence for the first we have nums[i-1]*nums[i]*nums[i+1]

If we start from the last balloon, we can determine  the left/right for the number
nums[-1]*nums[i]*nums[n]

Hence we start from the last balloon to be burst.

Recurrence: dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j


Runtime: O(n^3)
"""


def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    # add padding
    nums = [1] + nums + [1]

    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    return calculate(nums, dp, 0, n - 1)


def calculate(nums, dp, i, j):
    if dp[i][j] or j - i == 1:  # in memory or gap < 2
        return dp[i][j]

    coins = 0
    for k in range(i + 1, j):  # find the last balloon
        coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(nums, dp, i, k) + calculate(nums, dp, k, j))

    dp[i][j] = coins
    return coins
