#!/usr/bin/env python
"""
Given a list of words (without duplicates), write a program that returns all concatenated words
in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation:
"catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".


Solution 1: Based on word_break.py.
A word can only be formed by words shorter than it.
So we can first sort the input by length of each word, and only try to form one word by using words in front of it.

This solution gives TLE in leetcode.

Solution 2: Trie + DFS

"""


# Solution - 1

def find_all_concatenated_words_in_a_dict_1(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    if not words:
        return []

    result = []
    word_dict = []

    words.sort(cmp=compare)

    for word in words:
        if is_breakable(word, word_dict):
            result.append(word)

        word_dict.append(word)

    return result


def is_breakable(word, word_dict):
    if not word_dict:
        return False

    dp = [False] * (len(word) + 1)
    dp[0] = True

    for i in range(len(word) + 1):
        if not dp[i]:
            continue

        for item in word_dict:
            end = i + len(item)

            if end > len(word):
                continue

            if dp[end]:
                continue

            if item == word[i: end]:
                dp[end] = True

    return dp[-1]


def compare(a, b):
    if len(a) > len(b):
        return 1

    if len(a) == len(b):
        return 0

    if len(a) < len(b):
        return -1

# Solution - 2

    def find_all_concatenated_words_in_a_dict_2(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        result = []
        trie = Trie()

        # construct Trie tree
        for word in words:
            trie.insert(word)

        # test word is a concatenated word or not
        for word in words:
            if find(word, trie, 0, 0):
                result.append(word)

        return result


# 'count' means how many words during the search path
def find(word, trie, count, start):
    current = trie.root

    for i in range(start, len(word)):
        index = ord(word[i]) - ord('a')

        if not current.children[index]:
            return False

        if current.children[index].val == 1:
            if i == len(word) - 1:               # no next word, so test count to get result
                return count >= 1

            if find(word, trie, count + 1, start + 1):
                return True

        current = current.children[index]

    return False


class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if not p.children[index]:
                p.children[index] = TrieNode()

            p = p.children[index]

        p.val = 1
