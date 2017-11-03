#!/usr/bin/env python
'''
Reverse words in a sentence
'''
import sys


def get_reverse(sentence):

    print 'Original sentence: {}'.format(sentence)
   
    word_stack = []
    for word in sentence:
        word_stack.append(word)

    reverse = ''
    while word_stack:
        reverse += word_stack.pop()
        reverse += ' '


    print 'Reversed sentence: {}'.format(reverse)

def get_reverse_rec(sentence):
    if len(sentence) <= 1:
        return sentence[0]
    return get_reverse_rec(sentence[1:]) + ' ' + sentence[0]


def get_reverse_iter(sentence):
    m = 0
    n = len(sentence) - 1

    while (m < n):
        sentence[m], sentence[n] = sentence[n], sentence[m]
        m += 1
        n -= 1

    return ' '.join(sentence)


if __name__ == '__main__':
    #print get_reverse_rec(sys.argv[1:])
    #print get_reverse_iter(sys.argv[1:])
    

    # s = '  '
    if not s or len(s.strip()) == 0:
        return ''    
  
    # s = '  a'
    if len(s.split()) == 1:
        return s.strip()

    print get_reverse_iter('hello world!'.split())
