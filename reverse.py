#!/usr/bin/env python
'''
Reverse words in a string
'''
import sys


def get_reverse(word):
 
    print 'Original word {}'.format(word)
 
    # method 1 -faster
    #reverse = word[::-1]

    # method 2
    #reverse = ''.join(reversed(word))
 
    
    # method 3
    word_stack = []
    for i in word:
        word_stack.append(i)

    reverse = ''
    while word_stack:
        reverse += word_stack.pop()


    print 'Reversed word {}'.format(reverse)
 

def get_reverse_rec(word):
    if len(word) <= 1:
        return word
    return get_reverse_rec(word[1:]) + word[0]

def get_reverse_iter(word):
    if not word:
        return

    m = 0
    word_list= list(word)
    n = len(word_list) - 1

    while (m < n):
        word_list[m], word_list[n] = word_list[n], word_list[m]
        m += 1
        n -= 1

    return ''.join(word_list)



if __name__ == '__main__':
    res = get_reverse_iter(sys.argv[1])
    print res




