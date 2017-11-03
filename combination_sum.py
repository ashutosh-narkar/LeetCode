#!/usr/bin/env python
"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

**** The same repeated number may be chosen from C unlimited number of times.****

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ..., ak) must be in non-descending order.

The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[[7], [2, 2, 3]]


Solution:
The idea is to scan from the first to the last element from the ordered array.
check every possible combination of these numbers(multiple times for a single element).

the end condition of the dfs function is
1. the target == 0 , save list, return
2. the target < 0 return
3. start position >= array size return
otherwise, from for each element in the array, dfs(start, target-element value);
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return []

    # since non-descending order needed
    candidates.sort()

    result = []
    temp = []

    dfs(result, temp, candidates, 0, target)
    return result


def dfs(result, temp, candidates, start, target):
    if target < 0:
        return

    if target == 0:
        result.append(list(temp))
        return

    for i in range(start, len(candidates)):
        temp.append(candidates[i])
        dfs(result, temp, candidates, i, target - candidates[i])  # we pass 'i' and not 'i + 1' as duplicates allowed
        temp.pop()

if __name__ == '__main__':
    print combinationSum([2,3,6,7], 7)
