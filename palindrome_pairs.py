#!/usr/bin/env python
"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

Solution: The basic idea is to check each word for prefixes (and suffixes) that are themselves palindromes.

1) If you find a prefix that is a valid palindrome,
then the suffix reversed can be "prepended" with the word in order to make a palindrome

2) Similarly if you find a suffix that is a valid palindrome,
then the prefix reversed can be "appended" with the word in order to make a palindrome

Note that when considering suffixes, we explicitly leave out the empty string to avoid counting duplicates.
That is, if a palindrome can be created by appending an entire other word to the current word,
then we will already consider such a palindrome when considering the empty string as prefix for the other word.

Runtime: O(n * k^2), where n: total number of words; k: average length of each word
"""


def palindrome_pairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    if not words:
        return []

    result = []

    word_index = dict()
    for i, word in enumerate(words):
        word_index[word] = i

    for word, index in word_index.items():
        n = len(word)
        for i in range(n + 1):
            prefix = word[:i]
            suffix = word[i:]

            if is_palindrome(prefix):
                suffix_rev = suffix[::-1]
                if suffix_rev != word and suffix_rev in word_index:
                    result.append([word_index[suffix_rev], index])

            if i != n and is_palindrome(suffix):
                prefix_rev = prefix[::-1]
                if prefix_rev != word and prefix_rev in word_index:
                    result.append([index, word_index[prefix_rev]])

    return result


def is_palindrome(s):
    return s == s[::-1]
