#!/usr/bin/env python
'''
Given a string s and a dictionary of words dict, 
add spaces in s to construct a sentence where each word is a valid dictionary word.

Return ALL such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].


Analysis:
For the "Return all" problems, usually DFS or BFS will work well.

Instead of using a boolean array to track the match positions as we did in Word Break 1, 
we need to track the actual words. Then we can use "DFS" to get all the possible paths, i.e., the list of strings.

'''

import sys


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """

    if not s or not wordDict:
        return []

    breakable = [None] * (len(s) + 1)
    breakable[0] = []  # set initial value as empty list

    for i in range(len(s) + 1):

        # should continue from match position
        # Here we are specifically checking for a None value. Hence  if breakable[0] = [], this is True
        if breakable[i] is None:
            continue

        for word in wordDict:
            end = i + len(word)

            if end > len(s):
                continue

            if word == s[i: end]:
                if not breakable[end]:
                    breakable[end] = []

                breakable[end].append(word)

    # word is not breakable
    if breakable[-1] is None:
        return []

    result = []
    temp = []
    backtrack(result, temp, breakable, len(s))
    return result


def backtrack(result, temp, breakable, end):
    if end <= 0:
        path = temp[-1]
        for i in range(len(temp) - 2, -1, -1):
            path += " " + temp[i]
        result.append(path)
        return

    for word in breakable[end]:
        temp.append(word)
        backtrack(result, temp, breakable, end - len(word))
        temp.pop()

if __name__ == '__main__':
    s = "catsanddog",
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    
    print wordBreak(s, word_dict)







 
