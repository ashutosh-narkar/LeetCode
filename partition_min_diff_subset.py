#!/usr/bin/env python
"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that
the absolute difference between their sums is minimum.

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11

Solution: Similar to partition_equal_subset.py
"""

def find_min_diff(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return 0

    sumNums = sum(nums)

    dp = [[False] * (sumNums + 1) for _ in range(len(nums) + 1)]

    dp[0][0] = True

    # fill the first column
    # Picking nothing means 0. Thus dp[i][0] = true
    for i in range(1, len(nums) + 1):
        dp[i][0] = True

    # fill the first row
    for i in range(1, sumNums + 1):
        dp[0][i] = False

    for i in range(1, len(nums) + 1):
        for j in range(1, sumNums + 1):
            if j >= nums[i - 1]:           # if the current number is greater than the current sum, move on.
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

    diff = float('inf')
    # Find the largest j such that dp[n][j] = true
    # The idea is, sum of S1 is j and it should be closest
    # to sum/2, i.e., 2 * j should be closest to sum.
    for j in range(sumNums/2, -1, -1):
        if dp[len(nums)][j]:
            diff = sumNums - j * 2
            break

    return diff

if __name__ == '__main__':
    assert find_min_diff([1, 6, 11, 5]) == 1
    assert find_min_diff([10, 20, 15, 5, 25]) == 5
    print 'Test Passed'
