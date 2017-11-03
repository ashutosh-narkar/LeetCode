#!/usr/bin/env python
'''
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Analysis:
Let p be the position of element to be searched. Number of steps for finding high index 'h' is O(Log p).
The value of 'h' must be less than 2*p.
The number of elements between h/2 and h must be O(p). 
Therefore, time complexity of Binary Search step is also O(Log p) and overall time complexity is 2*O(Log p) which is O(Log p).
'''


def findPos(array, key):
    low = 0
    high = 1

    val = array[0]

    # find the upper limit to do Binary search
    while val < key:
        low = high
        high = 2 * high
        val = array[high]

    return binarySearch(array[low: high + 1])
