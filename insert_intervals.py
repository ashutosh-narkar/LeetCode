#!/usr/bin/env python
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


# @param intervals, a list of Intervals
# @param newInterval, a Interval
# @return a list of Interval

def insert(intervals, newInterval):
    res = []

    if not intervals:
        res.append(newInterval)
        return res

    # insert new interval
    intervals.append(newInterval)

    # sort list according to start value
    intervals.sort(key=lambda x:x.start)

    res.append(intervals[0])

    for i in range(1, len(intervals)):
        current = intervals[i]
        prev = res[-1]

        # check if current interval intersects with previous one
        if current.start <= prev.end:
            res[-1].end = max(res[-1].end, current.end)  # merge

        else:
            res.append(current)    # insert

    return res
