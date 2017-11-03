#!/usr/bin/env python
'''
3-Sum Problem
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = x? where is the desired sum
Find all unique triplets in the array which gives this sum.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4} and x = 0,
A solution set is:
(-1, 0, 1)
(-1, -1, 2)

Runtime O(n^2)
'''

def three_sum(numbers, desired_sum):
    if len(numbers) < 3:
        return

    result = set()

    # sort list
    numbers.sort()

    for i in range(len(numbers) - 2):

        a = numbers[i]

        # b + c = -a + desired_sum
        neg_a = -a + desired_sum
        
        start = i + 1
        end = len(numbers) - 1

        while (start < end):
            # Case1:
            if numbers[start] + numbers[end] == neg_a:
                val = (a, numbers[start], numbers[end])
                # since we want unique triplets 
                if val not in result:
                    result.add(val)
                start += 1
                end -= 1

            # Case2:
            if numbers[start] + numbers[end] < neg_a:
                start += 1
 
            else:
                end -= 1
            
    return result

if __name__ == '__main__':


    # Tests
    data = [-25, -10, -7, -3, 2, 4, 8, 10]
    print three_sum(data, 0)

    data = [-1,0,1,2,-1,-4]
    print three_sum(data, 0)
    
    data = [12, 3, 4, 1, 6, 9]
    print three_sum(data, 24)

    data = [1, 4, 45, 6, 10, 8]
    print three_sum(data, 22)















   
