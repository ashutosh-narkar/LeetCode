#!/usr/bin/env python
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Solution: Similar to isomorphic.py
"""


def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    data = str.split()

    if len(data) != len(pattern):
        return False

    d1 = {}  # {char: word}
    d2 = {}  # {word: char}

    for i in range(len(pattern)):
        ch = pattern[i]

        if ch in d1:
            if d1[ch] != data[i]:
                return False

        d1[ch] = data[i]

        if data[i] in d2:
            if d2[data[i]] != ch:
                return False

        d2[data[i]] = ch

    return True