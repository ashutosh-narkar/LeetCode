#!/usr/bin/env python
"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters.

You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Solution: Since each word contains 26 characters in lower case only.
We can use a bit map to encode the string. Since we only need 26 bits for a word,
it is enough to use an integer to encode a string.

Runtime: O(26 * n^2), which is O(n^2)
"""


def max_product(words):
    """
    :type words: List[str]
    :rtype: int
    """
    if not words:
        return 0

    encoded_words = [0] * len(words)

    for i in range(len(words)):
        word = words[i]
        for j in range(len(word)):
            index = ord(word[j]) - ord('a')  # lowercase only
            encoded_words[i] |= 1 << index

    max_prod = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (encoded_words[i] & encoded_words[j]) == 0:            # This is a BITWISE AND operation
                max_prod = max(max_prod, len(words[i]) * len(words[j]))
