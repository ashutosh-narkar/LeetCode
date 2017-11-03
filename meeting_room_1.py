#!/usr/bin/env python
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example, Given [[0, 30],[5, 10],[15, 20]], return false.
'''
# Solution: If a person can attend all meetings, there must not be any overlaps between any meetings.
# After sorting the intervals, we can compare the current end and next start.



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


def canAttendMeetings(intervals):
    '''

    :param intervals: List[Interval]
    :return:
    '''
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False

    return True
