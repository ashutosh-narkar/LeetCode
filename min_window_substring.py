#!/usr/bin/env python
"""
Finding the Minimum Window in S which Contains All Elements from T
OR
Given set of characters(T) and a string(S), find smallest substring which contains all characters

eg,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC"

This solution is similar to anagram_3.py and longest_substring_k_unq_chars.py
"""


def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if len(s) < len(t):
        return ""

    charCount = {}
    for ch in t:
        if ch in charCount:
            charCount[ch] += 1
        else:
            charCount[ch] = 1

    count = len(t)

    left = 0
    right = 0

    result = ""
    minlen = float("inf")

    while right < len(s):
        if s[right] in charCount:
            charCount[s[right]] -= 1

            if charCount[s[right]] >= 0:
                count -= 1

        # update the substring length and move the left pointer one step to the right
        # till we find the smallest substring that has all characters of T in it
        while count == 0:
            if right - left + 1 < minlen:
                minlen = right - left + 1
                result = s[left: right + 1]

            if s[left] in charCount:
                if charCount[s[left]] >= 0:
                    count += 1
                charCount[s[left]] += 1

            left += 1

        right += 1

    if minlen == float("inf"):
        return ""

    return result


if __name__ == '__main__':
    print min_window('this is a test string', 'tist')
