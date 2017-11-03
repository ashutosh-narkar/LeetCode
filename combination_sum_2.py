#!/usr/bin/env python
'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used **once** in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, .... , ak) must be in non-descending order.

The solution set must not contain duplicate combinations.


For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
'''


def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if not candidates:
        return []

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

    # keep track of previous number to avoid duplicates
    pre = -1
    for i in range(start, len(candidates)):
        if candidates[i] != pre:
            temp.append(candidates[i])
            dfs(result, temp, candidates, i + 1, target - candidates[i])  # we pass 'i + 1' and not 'i' as duplicates NOT allowed
            pre = candidates[i]
            temp.pop()

if __name__ == '__main__':
    print combinationSum2([2,3,6,7], 7)

