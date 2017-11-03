#!/usr/bin/env python

'''
f: String => Boolean
whether or not the string is a palindrome

f("abba") = true
f("chair") = false
f("Madam, I'm Adam!") = true
f("abba!!!!!!!!!!!!") = true
f('!!!!') = true

Ignore puctuations and do it in ONE-pass


Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.
'''

import sys

def isPalindrome(s):

    # empty string is assumed to be a palindrome 
    if not s:
        return True
        
    
    low = 0
    high = len(s) - 1
    
    
    while low < high:
        
        # move right till a alphanumeric char found
        while low < len(s) and not s[low].isalnum():
            low += 1

        if low == len(s):
            return True
            
        # move left till a alphanumeric char found
        while high >= 0 and not s[high].isalnum():
            high -= 1
       
        if high < 0:
            return True 
        
        if s[low].lower() != s[high].lower():
            return False
            
        low += 1
        high -= 1

    return True

if __name__ == '__main__':
    input = sys.argv[1]
    
    res = isPalindrome(input)
    if res:
        print '{} is a palindrome'.format(input)

    else:
        print '{} is not a palindrome'.format(input)













