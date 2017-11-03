#!/usr/bin/env python
'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S = [1,2,2], a solution is:

[
  [1],
  [2],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Solution:

When current element is same as previous one, then generate new subsets ONLY from the subsets generated from previous iteration, 
other than the whole subsets list.


Recursive solution has similar logic to Subset 1, Combination and Combination Sum 
'''
def subsetsWithDup(S):
    if not S:
        return []

    S.sort()
    
    result = []
 
    # we have to add empty set before the loop. Otherwise loop wont work correctly
    result.append([])
 
    # subsets (ie list of lists) created in previous iteration
    last = []

    for i  in range(len(S)):

        temp = [] 

        # if current =  previous, only use subsets created in previous iteration
        if i > 0 and S[i] == S[i - 1]:
            temp = map(list, last)                      # we cannot use temp = list(last). This will not create different objects
                                                        # for each of the sub-lists ie.they will be shared. 
                                                        # temp = copy.deepcopy(last) will work

        # use all subsets
        else:
            temp = map(list, result)

        last = []
        for item in temp:
            # add to list
            item.append(S[i])
            # update last
            last.append(item)
            # update result
            result.append(item)
        

    return result


# Recursive Solution
def subsetsWithDup_rec(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    nums.sort()

    result = []
    temp = []
    dfs(result, temp, nums, 0)
    return result


def dfs(result, temp, nums, start):
    result.append(list(temp))

    for i in range(start, len(nums)):
        # check to avoid duplicate numbers
        if i == start or nums[i] != nums[i - 1]:
            temp.append(nums[i])
            dfs(result, temp, nums, i + 1)
            temp.pop()


if __name__ == '__main__':
    print subsetsWithDup_rec([1,1])





 
