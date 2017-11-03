#!/usr/bin/env python
'''
Dutch National Flag Problem
Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[].
The functions should put all 0s first, then all 1s and all 2s in last
'''

def segregate(numbers):
    if not numbers:
        raise ValueError('No  input')

    low, mid  = 0, 0
    high = len(numbers) - 1

    # move low to a position where value is not 0
    while low < len(numbers) and numbers[low] == 0:
        low += 1  

    # move high to a position where value is not 2
    while(high >= 0 and numbers[high] == 2):  
        high -= 1  

    # set mid to low
    # swap with low if mid points to 0
    # swap with high if mid points to 2
    # increment mid if it points to 1
    mid = low

    # *************** less than equal to condition very very imp for accuracy *********************
    while (mid <= high):
        if numbers[mid] == 0:
            numbers[mid], numbers[low] = numbers[low], numbers[mid]
            mid += 1
            low += 1
            
        elif numbers[mid] == 1:
            mid += 1

        else:
            numbers[mid], numbers[high] = numbers[high], numbers[mid]
            high -= 1

    return numbers


if __name__ == '__main__':
    data = [2, 0, 1, 1, 2, 2, 0, 2, 1, 2, 1, 0]
    print 'Original {}'.format(data)

    res = segregate(data)
    print 'Segregated {}'.format(res) 
