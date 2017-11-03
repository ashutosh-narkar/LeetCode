#!/usr/bin/env python
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
find the minimum number of conference rooms required.
'''

# Solution:
# Very similar with what we do in real life. Whenever you want to start a meeting,
# you go and check if any empty room available (available > 0) and
# if so take one of them ( available -=1 ). Otherwise,
# you need to find a new room someplace else ( numRooms += 1 ).
# After you finish the meeting, the room becomes available again ( available += 1 ).


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def minMeetingRooms(intervals):
    start = []
    end = []

    for interval in intervals:
        start.append(interval.start)
        end.append(interval.end)

    start.sort()
    end.sort()


    available, numRooms = 0,0

    s, e = 0,0

    while s < len(start):
        if start[s] < end[e]:
            if available == 0:
                numRooms += 1
            else:
                available -= 1

            s += 1

        else:
            available += 1
            e += 1


    return numRooms