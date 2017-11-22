#!/usr/bin/env python
"""
Given a string which contains only lowercase letters, remove duplicate letters so that every
letter appear once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""


def remove_duplicate_letters(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ''

    # maintain character count
    remaining = dict()
    for ch in s:
        if ch in remaining:
            remaining[ch] += 1
        else:
            remaining[ch] = 1

    # track visited characters
    visited = set()
    result = list()

    for ch in s:
        if ch not in visited:

            # if the current character is lexicographically smaller than the last character on the stack and
            # the last character on the stack can occur in the future, then pop the stack. The popped character
            # will be added again later
            while result and ch < result[-1] and remaining[result[-1]] > 0:
                visited.remove(result.pop())

            visited.add(ch)
            result.append(ch)

        remaining[ch] -= 1

    return ''.join(result)
