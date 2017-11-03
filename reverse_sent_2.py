#!/usr/bin/env python
'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.

Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.

How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

Solution:
(1)Loop from start to the end of the string:
   (a) if current char is space and word string is empty, continue.
   (b) if current char is space but word string is NOT empty, which means we meet the end of word, then output the word, reset the word, continue.
   (c) if current char is non-space char, add this char to the word string, continue
(2)Handle the last word:
    (a) if the last word is empty, which means the input is empty, or the input has only spaces, or the last char/chars are spaces.  Then just remove the last space in the output string and return.
    (b) if the last word is not empty, add the last word to the front of the output string, then remove the last space in the output string and return.
'''
import sys 


def reverseWords(s):
    if not s:
        return ''

    res = '' # result string
    word = '' # single word string

    for ch in s:
        if ch == ' ' and not word:
            continue

        if ch == ' ':
            if word:
                if res: # add space between words
                    res = ' ' + res

                res = word + res
                word = ''

        if ch != ' ':
            word += ch

    if word:      # handle final word
        if res:
            res = ' ' + res
        res = word + res

    return res



if __name__ == '__main__':
    input = sys.argv[1]
    print 'Reverse of "{}" is "{}"'.format(input, reverseWords(input))









