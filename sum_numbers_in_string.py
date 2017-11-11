#!/usr/bin/env python
"""
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.

Examples:

Input:  1abc23
Output: 24

Input:  geeks4geeks
Output: 4

Input:  1abc2x30yz67
Output: 100

Input:  123abc
Output: 123
"""


def find_sum(s):
    if not s:
        return 0

    temp = ""
    result = 0

    for ch in s:
        if '0' <= ch <= '9':
            temp += ch
        elif temp:
            result += int(temp)
            temp = ""

    if temp:
        result += int(temp)

    return result


if __name__ == '__main__':
    assert find_sum('1abc23') == 24
    assert find_sum('geeks4geeks') == 4
    assert find_sum('1abc2x30yz67') == 100
    assert find_sum('123') == 123

    print 'Tests passed'
