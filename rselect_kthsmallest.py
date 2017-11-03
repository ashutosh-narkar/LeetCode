#!/usr/bin/env python
'''
Implement the Randomized Selection Algorithm
Given a list of unsorted integers, return the ith order statistic
(ie. ith smallest element in the list)
eg Find 2nd order statistic in [3,1,4,2]
Answer -> 2

Average Runtime O(n)
'''

from random import randint

def findKthSmallest(nums, k):
    '''
    Find the ith order statistic OR find ith smallest
    '''
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
        if nums[i] < pivot_value:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1

    # move the pivot element to correct position
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index

def main():
    '''
    Return the number of inversions
    '''
    data = [12, 14, 111, 0, -3, -2]
    order = 5
    # ith order statistic will be the element at
    # position i - 1 in the list
    res = findKthSmallest(data, order)
    print 'Input: {} Order: {} Result: {}'.format(data, order, res)

if __name__ == '__main__':
    main()
