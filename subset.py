#!/usr/bin/env python
'''
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
The easiest idea is using the binary numbers.
e.g.
set [a,b,c], write the binary numbers of length 3.
000    []
001    [a]
010    [b]
011    [ab]
100    [c]
101    [ac]
110    [bc]
111    [abc]

Time complexity : O(n*2^n) , for every input element loop traverses the whole solution set length i.e. 2^n
'''

def subsets(nums):

    # Elements in a subset must be in non-descending order
    nums.sort()

    num_subsets = 2 ** len(nums)

    result = [[] for _ in range(num_subsets)]

    for i in range(len(nums)):
        for j in range(num_subsets):
            if (j >> i) & 1:
                result[j].append(nums[i])
    return result




# See general Backtracking template at
# https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning
# Solution 2: Backtracking.

# Runtime for recursive sol:
# The number of recursive calls, T(n) satisfies the recurrence T(n) = T(n − 1) + T(n −
# 2) + · · · + T(1) + T(0), which solves to T(n) = O(2 ^n ). Since we spend O(n) time within a
# call, the time complexity is O(n2^n ).

# The space complexity is O(n) which comes from
# the maximum stack depth as well as the maximum size of a subset.




def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    # Elements in a subset must be in non-descending order
    nums.sort()
    result = []
    temp = []

    backtrack(result, temp, nums)
    return result


def backtrack(result, temp, nums, start=0):
    result.append(list(temp))       # make deep copy or it gets overwritten

    for i in range(start, len(nums)):
        temp.append(nums[i])
        backtrack(result, temp, nums, i + 1)
        temp.pop()
