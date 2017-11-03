#!/usr/bin/env python
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring.

The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''



def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    if not board:
        return False

    trie = Trie()
    for word in words:
        trie.insert(word)

    # result is kept as a 'set' to avoid duplicates in final result
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, trie, i, j, result, "")

    return list(result)


def dfs(board, trie, row, col, result, word):
    # invalid rows
    if row < 0 or row >= len(board):
        return

    # invalid columns
    if col < 0 or col >= len(board[0]):
        return

    # already visited
    if board[row][col] == ".":
        return

    word += board[row][col]

    # check prefix match for early loop termination
    if not trie.startsWith(word):
        return

    if trie.search(word):
        result.add(word)

    tmp = board[row][col]
    board[row][col] = "."

    dfs(board, trie, row - 1, col, result, word)
    dfs(board, trie, row + 1, col, result, word)
    dfs(board, trie, row, col - 1, result, word)
    dfs(board, trie, row, col + 1, result, word)

    board[row][col] = tmp




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