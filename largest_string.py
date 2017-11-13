#!/usr/bin/env python
"""
Given a list of strings words representing an English Dictionary, find the longest word in words that
can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input:
words = ["w","wo","wor","worl", "world"]

Output: "world"

Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

Output: "apple"

Explanation:
Both "apply" and "apple" can be built from other words in the dictionary.
However, "apple" is lexicographically smaller than "apply".

Solution:
1) Sort the words alphabetically, therefore shorter words always comes before longer words
2) Along the sorted list, populate the words that can be built
3) Any prefix of a word must comes before that word
"""


def longest_word(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if not words:
        return ""

    words = sorted(words)  # lexicographical order
    result = ""
    res = set()

    for word in words:
        if len(word) == 1 or word[:-1] in res:
            res.add(word)

            # update result
            if len(word) > len(result):
                result = word

    return result
