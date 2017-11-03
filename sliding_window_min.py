#!/usr/binenv python
'''
Sliding Window Minimum

Input: A long array A[], and a window width w
Output: An array B[], B[i] is the minimum value of from A[i] to A[i+w-1]
'''

from collections import deque


# Solution 1
def min_sliding_window(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []

    result = []
    queue = deque()  # store index

    for i, num in enumerate(nums):

        # Pop (from the end) indexes of elements greater than current number (they'll be useless).
        while queue and nums[queue[-1]] > num:
            queue.pop()

        # Append the index of the current number
        queue.append(i)

        # Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window)
        if queue[0] == i - k:
            queue.popleft()

        # If our window has reached size k, append the current window minimum to the output.
        if i >= k - 1:
            result.append(nums[queue[0]])    # The element at front of the Qi is the smallest
                                             # and element at rear of Qi is the largest of current window.

    return result



# Solution 2
def min_sliding_window(nums, k):
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

        # remove larger numbers as they are useless
        while queue and nums[i] < nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        # say k = 3, the first window is when i = 2.
        # since when 'i' reaches index 2, we have the first 3 (k) elements
        if i > k - 2:
            result.append(nums[queue[0]])

    return result










# DO NOT USE


def minSlidingWindow(numbers, w):
    if len(numbers) <= w:
        return min(numbers)

    q = deque()
    
    # first window
    for i in range(w):
        while(q  and numbers[i] <= numbers[q[-1]]):
            q.pop()

        q.append(i)

    b = []

    # remaining windows
    for i in range(w, len(numbers)):
        b.insert(i - w, numbers[q[0]])

        # Remove all elements larger than the currently
        # being added element (remove useless elements)
        while(q  and numbers[i] <= numbers[q[-1]]):
            q.pop()

        # Pop older elements outside window from q
        while(q and q[0] <= i - w):
            q.popleft()

        # Add current element at the rear of q
        q.append(i)


    # minimum element of last window
    b.insert(len(numbers) - w, numbers[q[0]])

    return b


if __name__ == '__main__':

    data = [1, 3, -1, -3, 5, 3, 6, 7]
    w = 3
    assert min_sliding_window(data, w) == [-1,-3,-3,-3,3,3]

    data = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    w = 3
    assert min_sliding_window(data, w) == [1,1,1,1,2,2,2]

    data = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    w = 4
    assert min_sliding_window(data, w) == [5,5,4,4,4,4,12]

    data = [12, 1, 78, 90, 57, 89, 56]
    w = 3
    assert min_sliding_window(data, w) == [1,1,57,57,56]

    print 'Tests passed'
