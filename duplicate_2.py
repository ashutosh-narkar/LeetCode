#!/usr/bin/env python
'''
Given a string, remove all 'b's and duplicate all 'a's
'''
import sys


def manipulate(s):
    s_list = list(s)

    i = 0
    while i < len(s_list):
        if s_list[i] == 'b':
            s_list.pop(i)

        elif s_list[i] == 'a':
            s_list.insert(i, s_list[i])
            i += 2

        else:
            i += 1 

    return ''.join(s_list)


if __name__ == '__main__':
    data = sys.argv[1]
    print 'original string {}'.format(data)
    print 'formatted string {}'.format(manipulate(data))
