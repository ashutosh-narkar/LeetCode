#!/usr/bin/env python
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Solution:
Compare the current char in the string with the previous one, if they are the same, count +1, 
if not, print the previous char (count + char), set the new char and count, until the string ends.
'''

import sys


def countAndSay(n):

    if n <= 0:
        return

    if n == 1:
        return '1'

    str1 = '1'
    strn = ''

    for i in range(1, n):
        strn = getSeq(str1)
        str1 =  strn
    return strn


def getSeq(s):
    prev = s[0]
    count = 1
    val = ''

    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1

        else:
            val += str(count) + prev
            prev = s[i]
            count = 1

    val += str(count) + prev

    return val


if __name__ == '__main__':
    print countAndSay(int(sys.argv[1]))
