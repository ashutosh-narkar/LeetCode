#!/usr/bin/env python
"""
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Solution: A classic dfs + backtracking problem. A trick here is if we've already abbreviated part of a word,
we must jump at least a character.

Runtime: O(2 ^ n)
"""


def general_abbrev(word):
    if not word:
        return []

    result = [word]
    backtrack(result, word, 0)
    return result


def backtrack(result, word, start):
    if start >= len(word):
        return

    for i in range(start, len(word)):
        j = 1
        while i + j <= len(word):
            num = str(j)
            abbr = word[:i] + num + word[i + j:]
            result.append(abbr)
            backtrack(result, abbr, i + len(num) + 1)
            j += 1




if __name__ == '__main__':
    print general_abbrev('word')