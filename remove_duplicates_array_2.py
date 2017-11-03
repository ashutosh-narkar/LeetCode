#!/usr/bin/env python

"""
Follow up for "Remove Duplicates"
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

Solution:
we need a count variable to keep how many times the duplicated element appears, if we encounter a different element,
just set counter to 1, if we encounter a duplicated one, we need to check this count,
if it is already k, then we need to skip it, otherwise, we can keep this element.
"""

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 2   # can be any number

    if len(nums) <= k:
        return len(nums)

    p = 1
    cnt = 1

    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[p] = nums[i + 1]
            p += 1
            cnt = 1

        else:
            if cnt < k:
                nums[p] = nums[i + 1]
                p += 1
                cnt += 1

    return p


if __name__ == '__main__':
    input = [1,1,1,2,2,3]

    print removeDuplicates(input) 
