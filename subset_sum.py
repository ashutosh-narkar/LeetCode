#!/usr/bin/env python
"""
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

Solution:
The problem is NP-Complete (There is no known polynomial time solution for this problem).

We can solve the problem in Pseudo-polynomial time using Dynamic programming.
We create a boolean 2D table subset[][] and fill it in bottom up manner.
The value of subset[i][j] will be true if there is a subset of set[0..i-1] with sum equal to j., otherwise false.
Finally, we return subset[n][sum]

****The dp logic is very similar to the 0/1 knapsack problem.****

"""


def isSubsetSum(nums, target):
    if not nums:
        return False

    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

    # We can get a sum of 0 by taking 0 numbers
    dp[0][0] = True

    # If we take 0 numbers we cannot get a non-negative sum
    for i in range(1, target + 1):
        dp[0][i] = False

    # If we don't pick a number, then sum is 0
    for i in range(1, len(nums) + 1):
        dp[i][0] = True

    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]    # either don't pick the number or pick it
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]  # dp[len(nums)][target]

if __name__ == '__main__':
    input = [3, 34, 4, 12, 5, 2]
    target = 9
    print isSubsetSum(input, target)

    input = [3, 2, 7, 1]
    target = 6
    print isSubsetSum(input, target)

    input = [3, 2, 7, 1, 8, 9]
    target = 100
    print isSubsetSum(input, target)




