#!/usr/bin/env python
'''

***** LOOK AT longest_substring_k_unq_chars.py

Given a string, find the longest substring that contains only two unique characters.
For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb"
'''

import sys

def subString(string):
    if not string:
        return

    unique_chars = []

    overall_max = ''
    current_max = ''

    for i in range(len(string)):
        if string[i] in unique_chars:
            current_max += string[i]

        else:
            if len(unique_chars) < 2:
                unique_chars.append(string[i])
                current_max += string[i]


            else:
                # save the result             
                overall_max = overall_max if len(overall_max) > len(current_max) else current_max
                 
                # char before the current char needs to stay
                char = string[i - 1]
                unique_chars = []
                unique_chars.append(char)
                
                # insert current char
                unique_chars.append(string[i]) 
   
  
                # current string should be started from
                # the first index where last character was continous
                # eg. 'bddda', so the new string should be
                # 'ddda'
                index = _get_index_char(string, i-1)
                current_max = string[index:i+1]


    # if string has only 2 unique character
    overall_max = overall_max if len(overall_max) > len(current_max) else current_max
    return overall_max



def _get_index_char(string, index):
    '''
    Given the string and index of character to trace
    return the index of first continous sequence of character

    eg _get_index_char('bddda', 3)
       >> 1
    '''
    char = string[index]
    while (index >= 0):
        if string[index] == char:
            index -= 1
        else:
            return index + 1

    # all characters from beginning are equal to desired char
    return 0

def run_tests():
    words = [('abcbbbbcccbdddadacb', 'bcbbbbcccb'),
             ('abcabcabcbcbc', 'bcbcbc'),
             ('aabbccccceeedd', 'ccccceee'),
             ('aabadefghaabbaagad', 'aabbaa'),
             ('abbbbbbbaaaaaaa', 'abbbbbbbaaaaaaa')]


    for word, expected in words:
        actual = subString(word)
        assert expected == actual, 'Error word {} actual {} expected {}'.format(word, actual, expected)
        print 'Longest substring with 2 chars in "{}" is "{}"'.format(word, actual)   



if __name__ == '__main__':
    #word  = sys.argv[1]
    #res =  subString(word)
    #print 'Longest substring with 2 chars in "{}" is "{}"'.format(word, res)   

    run_tests() 



















