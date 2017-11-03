#!/usr/bin/env python
'''
**** LOOK AT min_window_substring.py ****


Finding the Minimum Window in S which Contains All Elements from T
OR
Given set of characters(T) and a string(S), find smallest substring which contains all characters

eg,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC"
'''

import os
FILE_PATH = os.path.expanduser('~/misc/minwindow.txt')

def generate_ngrams(word, length):
    '''
    Return ngrams of given length
    eg generate_ngrams('kite', 2)
       >> ['ki', 'it', 'te']
    '''
    ngrams = zip(*[word[i:] for i in range(length)])
    # >> [('k', 'i'), ('i', 't'), ('t', 'e')]
    
    ngrams =[''.join(item) for item in ngrams]

    return ngrams



def find_smallest_substring(word, seq):
    '''
    Number of ngrams = len(word) - len(seq) + 1

    len(seq) <= smallest substring <= len(word)
    '''
    for i in range(len(seq), len(word) + 1):
        ngrams = generate_ngrams(word, i)

        for ngram in ngrams:
            if check_seq_in_ngram(seq, ngram):
                return ngram
    return

def check_seq_in_ngram(seq, ngram):

    # When a seq char matches a ngram char
    # we need to remove it
    # eg.  word = 'acbbaab'  seq = 'aab'  expected = 'baa'
    # we will get 'acb' if we do not remove matched chars
    # Also we need to preserve the original ngram
    
    #temp = ngram
    #for i in seq:
    #    if i not in temp:
    #        return False
    #    else:
    #        temp = temp.replace(i, '', 1)
    #return True

    # we only need to check if all chars in 'seq' are in ngram
    # we DO NOT need the actual substring here
    # This is modified ANAGRAM problem

    word_count = {}

    for i in ngram:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1


    for i in seq:
        if i not in word_count:
            return False

        word_count[i] -= 1
        if word_count[i] == 0:
            del(word_count[i])

    return True


if __name__ == '__main__':
     
    # load test cases
    with open(FILE_PATH, 'r') as f:
        lines =  f.readlines()
        for line in lines:
            word, seq, expected_ans = line.split()
            actual_ans = find_smallest_substring(word, seq)
            assert actual_ans == expected_ans, 'Error case: word {} seq {} expected {} actual {}'.format(word, seq, expected_ans, actual_ans)  

