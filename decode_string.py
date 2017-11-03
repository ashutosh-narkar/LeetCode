#!/usr/bin/env python
'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for
those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    stack = []
    curNum = 0
    curStr = ""

    for ch in s:
        if ch.isdigit():
            curNum = curNum * 10 + int(ch)  # it's like str to int

        elif ch == '[':
            stack.append(curStr)
            stack.append(curNum)

            # reset
            curNum = 0
            curStr = ""

        elif ch == ']':
            num = stack.pop()
            prevStr = stack.pop()

            curStr = prevStr + num * curStr

        else:
            curStr += ch

    return curStr