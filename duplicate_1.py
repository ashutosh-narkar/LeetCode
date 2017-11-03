#!/usr/bin/env python
'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''

# Solution 1: Space O(n) Time O(n)
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False
                                                                
    numbers = set()
                                                                        
    for num in nums:
        if num in numbers:
            return True
        numbers.add(num)
                                                                                                                                        
    return False


# Solution 2: Space O(1) Time O(NlogN)
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False
                                                                
    nums.sort()
                                                                        
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
                                                                                                                                        
    return False

