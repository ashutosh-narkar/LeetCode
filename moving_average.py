#!/usr/bin/env python
'''
Given an array and window size, return the running average in the window size.

**** Similar logic works for sliding max and sliding min ****

'''

from collections import deque

def runningAverageWindow(numbers, w):
    if len(numbers) <= w:
        return sum(numbers)/ float(len(numbers))

    result = []
    
    # first window
    window_items = deque(numbers[:w])
    avg = sum(window_items) / float(w)
    
    # remaining windows
    for i in range(w, len(numbers)):
        result.insert(i - w, avg)
    
        # add new element and remove oldest element from queue     
        window_items.append(numbers[i])
        window_items.popleft()
 
        avg = sum(window_items) / float(w)

    # average of last 'w' numbers  
    result.insert(len(numbers) - w, avg)
    return result

if __name__ == '__main__':
    data = [1,2,3,4,5,6]
    w = 3
    assert runningAverageWindow(data, w) == [2, 3, 4, 5]
    
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    w = 3
    assert  runningAverageWindow(data, w) == [1.0, -1/float(3), 1/float(3), 5/float(3), 14/float(3), 16/float(3)]

    print 'Tests passed'        
