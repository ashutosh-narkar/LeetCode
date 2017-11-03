#!/usr/bin/env python
'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

'''
O(n)solution is complicated. See links below
https://github.com/kamyu104/LeetCode/blob/master/Python/wiggle-sort-ii.py
https://discuss.leetcode.com/topic/41464/step-by-step-explanation-of-index-mapping-in-java
https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing
https://discuss.leetcode.com/topic/71990/summary-of-the-various-solutions-to-wiggle-sort-for-your-reference
'''



# Sorting and reorder solution - 1
# Time - O(nlogn)
# Space - O(n)
def wiggleSort(self, nums):
    if not nums:
        return

    temp = sorted(nums)

    # At this point the numbers in temp are sorted in ascending order
    # Now move larger numbers in odd places of 'nums' and
    # move the smaller numbers in even places

    for i in range(1, len(nums), 2) + range(0, len(nums), 2):
        nums[i] = temp.pop()




# Sorting and reorder solution - 2
# Time - O(nlogn)
# Space - O(1)
def wiggleSort(nums):
    nums.sort()
    med = (len(nums) - 1) / 2

    # At this point the numbers are sorted in ascending order
    # Now move larger numbers (ie numbers to right of mid) in odd places of 'nums' and
    # move the smaller numbers (ie numbers to left of mid) in even places

    nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]   # Syntax num[start:end:step]

