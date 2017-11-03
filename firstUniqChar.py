#!/usr/bin/env python
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return -1

    if len(s) == 1:
        return 0

    # build a character count array
    charCount = getCharCountArray(s)

    for i, ch in enumerate(s):
        if charCount[ord(ch)] == 1:
            return i
    return -1


def getCharCountArray(s):
    NO_OF_CHARS = 256
    charCount = [0] * NO_OF_CHARS

    for ch in s:
        charCount[ord(ch)] += 1

    return charCount