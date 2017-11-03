#!/usr/bin/env python
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Solution: Use Bucket Sort. Runtime O(n)
'''


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # Create 'n + 1' empty buckets since frequency of number will be used to index into the bucket list
    bucket = [[] for _ in range(len(nums) + 1)]

    # count the frequency for each element
    frequencyMap = {}
    for num in nums:
        if num in frequencyMap:
            frequencyMap[num] += 1

        else:
            frequencyMap[num] = 1

    # Use freq of the number to index into the bucket list
    for num, freq in frequencyMap.items():
        bucket[freq].append(num)

    result = []

    # scan bucket list from the back
    for i in range(len(bucket) - 1, -1, -1):
        if not bucket[i]:
            continue

        else:
            result.extend(bucket[i])
            if len(result) == k:
                break

    return result
