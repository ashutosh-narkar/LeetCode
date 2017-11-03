#!/usr/bin/env python
'''
Maximum Gap problem
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

http://cgm.cs.mcgill.ca/~godfried/teaching/dm-reading-assignments/Maximum-Gap-Problem.pdf
Runtime - O(n)
'''

import math

def maximumGap(nums):

    # base case
    if len(nums) < 2:
        return 0

    max_num = nums[0]
    min_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

        elif num < min_num:
            min_num = num

    bucket_size = 1 + (max_num - min_num) / (len(nums) - 1)

    bucket_min_max = [(float('inf'), float('-inf')) for i in range(len(nums))]

    for num in nums:
        index = (num - min_num) / bucket_size
        bucket_min_max[index] = (min(bucket_min_max[index][0], num), max(bucket_min_max[index][1], num))

  

    possible_buckets = []
    for item1, item2 in bucket_min_max:
        if item1 != float('inf')  and item2 != float('-inf'):
            possible_buckets.append((item1, item2))  

    if len(possible_buckets) == 1:
        return possible_buckets[0][1] - possible_buckets[0][0]


    gap = 0
    last_max = possible_buckets[0][1]

    for bucket_min, bucket_max in possible_buckets[1:]:
        if bucket_min == float('inf'):
            continue
        gap = max(gap, bucket_min - last_max)
        last_max = bucket_max

    return gap

if __name__ == '__main__':
    data = [100, 3, 2, 1]
    max_gap = maximumGap(data)
    assert max_gap == 97


    data = [2, 5, 1, 10, 6, 11]
    max_gap = maximumGap(data)
    assert max_gap == 4

    data = [3, 6, 9, 1]
    max_gap = maximumGap(data)
    assert max_gap == 3
    
    data = [1,10000000]
    max_gap = maximumGap(data)
    assert max_gap == 9999999 

    print 'Tests passed'


