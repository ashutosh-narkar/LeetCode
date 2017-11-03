#!/usr/bin/env python
'''
Sliding Window Maximum
A long array A[] is given to you. There is a sliding window of size w which is 
moving from the very left of the array to the very right.
You can only see the w numbers in the window. 
Each time the sliding window moves rightwards by one position. 

Following is an example:
The array is [1 3 -1 -3 5 3 6 7], and w is 3.
Output = [3,3,5,5,6,7]

Idea:
Maintain a double ended queue of capacity w, that stores only useful elements of current window of w elements. 
An element is useful if it is in current window and is greater than all other elements on left side of it in current window. 
We process all array elements one by one and maintain Qi to contain useful elements of current window and 
these useful elements are maintained in sorted order. 
The element at front of the Qi is the largest and element at rear of Qi is the smallest of current window.


Runtime O(n). This is because each element in the list is being inserted and then removed at most once.
Therefore, the total number of insert + delete operations is 2n.
'''

from collections import deque


# Solution 1:
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []

    result = []
    queue = deque()  # store index of the numbers

    for i, num in enumerate(nums):

        # Pop (from the end) indexes of elements smaller than current number (they'll be useless).
        while queue and nums[queue[-1]] < num:
            queue.pop()

        # Append the index of the current number
        queue.append(i)

        # Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window)
        if queue[0] == i - k:
            queue.popleft()

        # If our window has reached size k, append the current window maximum to the output.
        if i >= k - 1:
            result.append(nums[queue[0]])   # The element at front of the Qi is the largest
                                            # and element at rear of Qi is the smallest of current window.

    return result




# Solution 2
def max_sliding_window(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []

    result = []
    queue = deque()  # store index

    for i in range(len(nums)):

        # remove numbers that are out of the window
        if queue and queue[0] < i - k + 1:
            queue.popleft()

        # remove smaller numbers as they are useless
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        # say k = 3, the first window is when i = 2.
        # since when 'i' reaches index 2, we have the first 3 (k) elements
        if i > k - 2:
            result.append(nums[queue[0]])

    return result





# DO NOT USE

def maxSlidingWindow(numbers, w):
    if len(numbers) <= w:
        return max(numbers)

    q = deque()
    # Initialize deque for first window
    # For very element, the previous smaller elements are useless
    # so remove from queue
    for i in range(w):
        while(q and numbers[i] >= numbers[q[-1]]):
            q.pop()

        q.append(i)

    b = []
    for i in range(w, len(numbers)):
        b.insert(i - w, numbers[q[0]])

        # Remove all elements smaller than the currently
        # being added element (remove useless elements)
        while(q and numbers[i] >= numbers[q[-1]]):
            q.pop()

        # Pop older elements outside window from q
        while(q and q[0] <= i - w):
            q.popleft()
     
        # Add current element at the rear of q
        q.append(i)
    
    # maximum element of last window
    b.insert(len(numbers) - w, numbers[q[0]])

    return b
    

if __name__ == '__main__':

    data = [1, 3, -1, -3, 5, 3, 6, 7]
    w = 3
    assert max_sliding_window(data, w) == [3,3,5,5,6,7]

    data = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    w = 3
    assert max_sliding_window(data, w) == [3, 3, 4, 5, 5, 5, 6]

    data = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    w = 4
    assert max_sliding_window(data, w) == [10, 10, 10, 15, 15, 90, 90]

    data = [12, 1, 78, 90, 57, 89, 56]
    w = 3
    assert max_sliding_window(data, w) == [78, 90, 90, 90, 89]

    print 'Tests passed'







