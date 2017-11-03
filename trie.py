#!/usr/bin/env python
'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

'''


class TrieNode(object):
    def __init__(self):
        self.value = 0
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.value = 1  # make value = 1 for the leaf node of a complete word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                return False
            p = p.children[idx]

        if p.value == 1:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                return False
            p = p.children[idx]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)