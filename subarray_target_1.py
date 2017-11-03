#!/usr/bin/env python
'''
Find subarray with given sum
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found

There may be more than one subarrays with sum as the given sum. The following solutions print first such subarray.
'''


def subArraySum(nums, target):
    if not nums:
        return

    index = 0
    res = nums[0]
 
    for i in range(1, len(nums) + 1):
        res = sum(nums[index: i])
  
        if res == target:
            return (index, i)

        elif res < target:
            continue

        else:
            # if sum becomes greater than target, move index forward till sum becomes <= target
            # make sure index is less than i - 1, since the last number in current sum is element at index "i - 1"
            while res > target and index < i - 1:
                index += 1
                res = sum(nums[index:i])

            if res == target:
                return (index, i)
 




if __name__ == '__main__':
    input  = [1, 4, 20, 3, 10, 5]
    target = 33
 
    start, end = subArraySum(input, target)
    print 'Subarray for target {} is {}\n'.format(target, input[start: end])

    input  = [1, 4, 0, 0, 3, 10, 5]
    target = 7
 
    start, end = subArraySum(input, target)
    print 'Subarray for target {} is {}\n'.format(target, input[start: end])


    input  = [1, 4]
    target = 0
 
    res = subArraySum(input, target)
    if not res:
        print 'Subarray for target {} is []\n'.format(target)


    input  = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
 
    start, end = subArraySum(input, target)
    print 'Subarray for target {} is {}\n'.format(target, input[start: end])


    input  = [23, -3, 15, -90, -9, 45, 60, 32, -89]
    target = -39

    start, end = subArraySum(input, target)
    print 'Subarray for target {} is {}\n'.format(target, input[start: end])
 

    input = [-5, 5]
    target = 0
 
    start, end = subArraySum(input, target)
    print 'Subarray for target {} is {}\n'.format(target, input[start: end])


    print 'Test Passed '

