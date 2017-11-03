#!/usr/bin/env python
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.
'''

from random import randint

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    if not nums:
        return -1

    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1

    while left <= right:
        new_pivot_idx = partitionAroundPivot(left, right, nums)

        if new_pivot_idx == k - 1:
            return nums[new_pivot_idx]

        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1

        else:  # new_pivot_idx < k - 1.
            left = new_pivot_idx + 1


def partitionAroundPivot(left, right, nums):
    pivot_idx = randint(left, right)
    pivot_value = nums[pivot_idx]
    store_index = left

    # move pivot element to rightmost end
    nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

    for i in range(left, right):
        if nums[i] > pivot_value:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1

    # move the pivot element to correct position
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index


def main():

    data = [-4, -2, -3, -5, 0]
    order = 1

    res = findKthLargest(data, order)
    print 'Input: {} Order: {} Result: {}'.format(data, order, res)

if __name__ == '__main__':
    main()