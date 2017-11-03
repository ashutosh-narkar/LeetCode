#!/usr/bin/env python
'''
Palindrome Checker
'''

import sys
import string
import re
from collections import deque

def is_palindrome(word):

    q = deque(word)

    while q:
        try:
            a = q.popleft()
            b = q.pop()
        except IndexError, e:
            # this means only one element in queue
            return True
        else:
            if a != b:
                return False

         
    return True

def is_palindrome_2(word):
    return word == word[::-1]


def is_palindrome_rec(word):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False
    return is_palindrome_2(word[1:-1])


def is_palindrome_iter(word):
    m = 0
    n = len(word) - 1
 
    while(m < n):
        if word[m] != word[n]:
            return False

        m += 1
        n -= 1

    return True 
 

def _pre_process_input(data):
    '''
    If the string is a sentence remove punctuations and spaces.
    Also convert string to lowercase
    '''
    if len(data.split()) > 1:
        #data = data.translate(string.maketrans("",""), string.punctuation)
        #data = data.replace(" ", "")
        data = re.findall('\w', data)
        data = ''.join(data)  

    return data.lower()


if __name__ == '__main__':
    data = sys.argv[1]
    data = _pre_process_input(data)
   
    if is_palindrome_rec(data):
        print 'REC method - {} is a palindrome'.format(data)
    else:
        print 'REC method - {} is NOT a palindrome'.format(data)

    if is_palindrome_iter(data):
        print 'ITER Method - {} is a palindrome'.format(data)
    else:
        print 'ITER Method - {} is NOT a palindrome'.format(data)
