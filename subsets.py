#!/usr/bin/env python
'''
LOOK FOR SOLUTION AT SUBSET.PY


Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Solution:
Recursive solution has similar logic to Combination and Combination Sum 

Runtime for recursive sol:
The number of recursive calls, T(n) satisfies the recurrence T(n) = T(n − 1) + T(n −
2) + · · · + T(1) + T(0), which solves to T(n) = O(2 ^n ). Since we spend O(n) time within a
call, the time complexity is O(n2^n ). 

The space complexity is O(n) which comes from
the maximum stack depth as well as the maximum size of a subset.
'''

def subsets(S):
    if not S:
        return []

    S.sort()
    result = []

    for i  in range(len(S)):
        nums = []

        # get the sets already in result
        nums = map(list, result)                   # ******DO NOT EDIT ITEMS IN ORIGINAL RESULT*******

        # add current element to existing sets
        for item in nums:
            item.append(S[i])

        # add current element itself
        nums.append([S[i]])

        result.extend(nums)

    # add empty set. DO NOT add before loop
    result.append([])

    return result


def subsets_rec(S):
    if not S:
        return []

    S.sort()
    
    result = []
    dfs(S, result)

    # add empty set
    result.append([])
    return result


def dfs(S, result, start=0, nums=[]):
    
    if len(nums) == len(S):
        return
    
    for i in range(start, len(S)):
        nums.append(S[i])
        result.append(list(nums))
        dfs(S, result, i + 1, nums)
        nums.pop()



if __name__ == '__main__':
    print subsets_rec([1,2,3])





 
