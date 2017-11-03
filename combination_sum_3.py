#!/usr/bin/env python
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Use DFS. Same logic as subsets, combination_sum and combination_sum2

Example 1:
Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:
Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]
'''


def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    result = []
    temp = []

    dfs(result, temp, 1, n, k)  # '1' since we can use numbers 1 to 9
    return result


def dfs(result, temp, start, target, k):
    if target < 0:
        return

    if target == 0 and k == 0:
        result.append(list(temp))
        return

    for i in range(start, 10):  # we use numbers 1 to 9
        temp.append(i)
        dfs(result, temp, i + 1, target - i, k - 1)  # 'i + 1' since each combination should be a unique set of numbers
        temp.pop()
