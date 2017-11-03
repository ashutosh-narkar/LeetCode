#!/usr/bin/env python
'''
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


Solution:
Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not.
Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers.
If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.

Base case: dp[0][0] is true; (zero number consists of sum 0 is true)

Transition function:
For each number, if we don't pick it, dp[i][j] = dp[i-1][j], which means if the first i-1 elements has made it to j,
dp[i][j] would also make it to j (we can just ignore nums[i]).

If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i]
and the remaining composed of other previous numbers.

Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

'''
def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False

    sumNums = sum(nums)

    # If sum is odd, there can not be two subsets
    # with equal sum, so return false.
    if sumNums % 2:
        return False

    sumNums /= 2

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

    return dp[-1][-1]  # dp[len(nums)][sumNums]


# Same solution as above but with 1-D array
def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False

    sumNums = sum(nums)

    # If sum is odd, there can not be two subsets
    # with equal sum, so return false.
    if sumNums % 2:
        return False

    sumNums /= 2

    dp = [False] * (sumNums + 1)

    dp[0] = True

    for num in nums:
        for i in range(sumNums, num - 1, -1):  # since the current number should not exceed the current sum
            dp[i] = dp[i] or dp[i - num]

    return dp[-1]