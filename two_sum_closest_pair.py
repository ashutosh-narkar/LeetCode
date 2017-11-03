#!/usr/bin/env python
'''
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.
'''

def twoSumClosest(arr1, arr2, target):
    # both empty
    if not (arr1 or arr2):
        return

    # one of them is empty
    if not (arr1 and arr2):
        return 


    min_diff = float('inf')
    result = None


    m = 0
    n = len(arr2) - 1


    while m < len(arr1) and n >= 0:
        curr_sum = arr1[m] + arr2[n]

        if curr_sum == target:
            return (arr1[m], arr2[n])

        diff = abs(target - curr_sum)

        if diff < min_diff:
            min_diff = diff
            result = (arr1[m], arr2[n])


        if curr_sum < target:
            m += 1

        else:
            n -= 1


    return result

if __name__ == '__main__':
    print twoSumClosest([1, 4, 5, 7], [10, 20, 30, 40], 32)
    print twoSumClosest([1, 4, 5, 7], [10, 20, 30, 40], 50)
    print twoSumClosest([1, 4, 5, 7], [10, 20, 30, 40], 38)
