#!/usr/bin/env python
"""
Given two 1d vectors, implement an iterator to return their elements alternately.
For example, given two 1d vectors:
v1 = [1, 2]
v2 = [3, 4, 5, 6]

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
"""


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = []
        self.queue.append(v1)
        self.queue.append(v2)

    def next(self):
        """
        :rtype: int
        """
        first_list = self.queue.pop(0)
        first_element = first_list.pop(0)

        if first_list:
            self.queue.append(first_list)

        return first_element

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True
        return False

if __name__ == '__main__':
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]

    zigzag = ZigzagIterator(v1, v2)

    while zigzag.hasNext():
        print zigzag.next()
