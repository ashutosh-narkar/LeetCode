#!/usr/bin/env python
"""
You are given a string, S, and a list of words, L, that are all of the same length.
Find all starting indices of substring(s) in S that is a concatenation of each word in L
exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

NOTE: This solution gives Time Limit Exceeded (TLE) in leetcode

"""
def findSubstring(S, L):

    if not L:
        return

    word_count = {}
    for word in set(L):
        word_count[word] = L.count(word)

    # OR use our normal approach
    #for word in L:
    #    if word not in word_count:
    #        word_count[word] = 1

    #    else:
    #        word_count[word] += 1

    len_word = len(L[0])
    total_words = len_word * len(L)    # window size

    first_word = S[:total_words]

    result = []
    index = 0

    while len(first_word) >= total_words:
        if check_words(first_word, word_count):
            result.append(index)

        index += 1
        
        first_word = S[index: index + total_words]

    return result


def check_words(word, word_dict):

    copy_dict = {}
    
    # length of each word
    len_word = len(word_dict.keys()[0])

    index = 0
    
    while index < len(word):
        target = word[index: index + len_word]
        if target not in copy_dict:
            copy_dict[target] = 1

        else:
            copy_dict[target] += 1
             
        index += len_word

    return copy_dict == word_dict

if __name__ == '__main__':
    S = "barfoothefoobarman"
    L = ["foo", "bar"]

    print findSubstring(S, L)


    S = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
    L = ["fooo","barr","wing","ding","wing"]
    print findSubstring(S, L)

    
    S = "aaa"
    L = ["a","a"]
    print findSubstring(S, L)
   
    S = 'aaaaaaaa'
    L = ["aa","aa","aa"]
    print findSubstring(S, L)   # expected ans -> [0,1,2]


