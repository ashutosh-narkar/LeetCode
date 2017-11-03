#!/usr/bin/env python
'''
Given a string and a dictionary of words , 
determine if the string can be segmented into a space-separated 
sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].
output = ["leet", "code"]

Solution:
Define an array t[] such that t[i]==true -> s[0: i] can be segmented using dictionary
Initial state t[0] == true

O(string length * dict size)
'''
import sys

word_dict = ['leet', 'code', "cat", "cats", "and", "sand", "dog"]


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    if not s or not wordDict:
        return False

    breakable = [False] * (len(s) + 1)
    breakable[0] = True  # set initial state True

    for i in range(len(s) + 1):
        if not breakable[i]:
            continue

        # should continue from match position
        for word in wordDict:
            end = i + len(word)
            if end > len(s):
                continue

            # if already set
            if breakable[end]:
                continue

            if word == s[i:end]:
                breakable[end] = True

    return breakable[-1]


if __name__ == '__main__':
    
    test_words = ['leetcode', 'catsanddog', 'catsanded', 'andcode', 'dogcoded', 'blah']
    expected = [True, True, False, True, False, False]
   
    for i in range(len(test_words)):
        res = wordBreak(test_words[i], word_dict)
        assert res == expected[i]

    print 'Test passed'








 
