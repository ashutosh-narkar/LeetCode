#!//usr/bin/env python
"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3

Similar Problems Explanation:
https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs/2

Similar Problems:
count_of_smaller_numbers_after_self.py
count_of_range_sum.py
"""


def reverse_pairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    return count_while_merge_sort(nums, 0, len(nums))


def count_while_merge_sort(nums, start, end):
    if end - start <= 1:
        return 0

    mid = start + (end - start) / 2

    count = count_while_merge_sort(nums, start, mid) + count_while_merge_sort(nums, mid, end)

    j = mid
    for i in range(start, mid):
        while j < end and nums[i] > 2 * nums[j]:
            j += 1
            count += mid - i

    nums[start: end] = sorted(nums[start:  end])

    return count
