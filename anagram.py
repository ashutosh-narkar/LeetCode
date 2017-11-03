#!/usr/bin/env python
'''
Given two strings detect if they are anagrams
'''

def is_anagram(a, b):
    
    if len(a) != len(b):
        return False

    word_count = {}
    for i in a:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    for i in b:
        if i not in word_count:
            return False
        word_count[i] -= 1
        if word_count[i] == 0:
            del word_count[i]

    return True



if __name__ == '__main__':
    words = [('heir', 'hire'), ('hoes', 'hose'), ('icon', 'coin'), ('drier', 'rider'), ('fiber', 'blah'), ('unbred', 'boored'), ('vector', 'covert')]
    expected = [True, True, True, True, False, False, True]

    for i in range(len(words)):
        word1, word2 = words[i]
        res = is_anagram(word1, word2)
        assert res == expected[i]

    for i in range(len(words)):
        word1, word2 = words[i]
        res = is_anagram2(word1, word2)
        assert res == expected[i]
    
    print 'Tests passed'
