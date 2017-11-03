#!/usr/bin/env python
'''
Given two strings S and T, determine if they are both one edit distance apart.
'''

import sys


def isOneEditDistance(s, t):

    if not s or not t:
        return False

    m = len(s)
    n = len(t)

    if abs(m - n) > 1:
        return False

    i = 0
    j = 0
    count = 0

    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1

        else:
            count += 1

            if count > 1:
                return False

            # decide which pointer to move ahead
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1

    if i < m or j < n:
        count += 1

    if count == 1:
        return True

    return False

if __name__ == '__main__':
    s, t = sys.argv[1:]

    if isOneEditDistance(s, t):
        print '{} and {} are at edit distance 1'.format(s, t)

    else:
        print '{} and {} are NOT at edit distance 1'.format(s, t)


            
