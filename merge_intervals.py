#!/usr/bin/env python
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Solution:
# Just go through the intervals sorted by start coordinate and
# either combine the current interval with the previous one if they overlap,
# or add it to the output by itself if they don't.



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x.start)
    out = []

    for interval in intervals:
        if out and interval.start <= out[-1].end:
            out[-1].end = max(out[-1].end, interval.end)

        else:
            out.append(interval)

    return out