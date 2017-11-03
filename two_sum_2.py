#!/usr/bin/env python
'''
Given an array of integers that is ALREADY sorted in ASCENDING order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. 

Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
def twoSum(numbers, target):
    if not numbers or not target:
        return

    start = 0
    end = len(numbers) - 1

    while start < end:
        sum = numbers[start] + numbers[end]

        if sum == target:
            return [start + 1, end+ 1]  # non zero-based indexes

        elif sum < target:
            start += 1
  
        else:
            end -= 1


    return []




if __name__ == '__main__':
    input = [2, 7, 11, 15]
    print twoSum(input, 9) 
