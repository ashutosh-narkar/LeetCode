#!/usr/bin/env python
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
'''

# Solution 1:  Use a dict to record all nums appeared in the first list,
# and then check if there are nums in the second list have appeared in the dict.

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    map = {}
    for i in nums1:
        map[i] = map[i] + 1 if i in map else 1

    for j in nums2:
        if j in map:
            res.append(j)
            map[j] -= 1

            if map[j] == 0:
                del map[j]

    return res

# Solution 2: Sort and check
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    nums1.sort()
    nums2.sort()
    i = j = 0

    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            # if not (len(res) and nums1[i] == res[len(res)-1]):
            res.append(nums1[i])
            i += 1
            j += 1

    return res