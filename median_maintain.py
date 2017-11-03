#!/usr/bin/env python
"""
Median is the middle value in an ordered integer list.
 If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

"""
from heapq import *

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.max_heap or num > -self.max_heap[0]:
            heappush(self.min_heap, num)

            # check if heaps need to be rebalanced
            if len(self.min_heap) > len(self.max_heap) + 1:
                heappush(self.max_heap, -heappop(self.min_heap))

        else:
            heappush(self.max_heap, -num)

            # check if heaps need to be rebalanced
            if len(self.max_heap) > len(self.min_heap) + 1:
                heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self):
        """
        :rtype: float
        """

        # if the heaps have same length, it means the total array has even number of elements
        if len(self.min_heap) == len(self.max_heap):
            median = (self.min_heap[0] + (-self.max_heap[0])) * 0.5
            return median

        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()