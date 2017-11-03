#!/usr/bin/env python
"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


def valid_palindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """

    if not s:
        return []

    low = 0
    high = len(s) - 1

    # mismatch count
    count_1 = 0

    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1

        # on mismatch, move the high pointer one step to the left
        else:
            count_1 += 1
            high -= 1

    low = 0
    high = len(s) - 1

    # mismatch count
    count_2 = 0

    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1

        # on mismatch, move the low pointer one step to the right
        else:
            count_2 += 1
            low += 1

    return count_1 <= 1 or count_2 <= 1