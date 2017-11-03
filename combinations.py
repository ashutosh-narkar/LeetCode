#!/usr/bin/env python
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Use DFS. Same logic as subsets, combination_sum and combination_sum2
'''


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if n < 1 or k < 1 or n < k:
        return []

    result = []
    temp = []

    dfs(result, temp, 1, n, k)
    return result


def dfs(result, temp, start, n, k):
    if k == 0:
        result.append(list(temp))
        return

    for i in range(start, n + 1):
        temp.append(i)
        dfs(result, temp, i + 1, n, k - 1)
        temp.pop()


if __name__ == '__main__':
    print combine(4, 2)
