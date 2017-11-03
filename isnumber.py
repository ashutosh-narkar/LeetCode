#!/usr/bin/env python
'''
Check if a String contains a number or not
'''

import sys
import re

def containsNumber1(word):
    '''
    The character "0" has the ASCII value 48
    so subtract 48 from every ASCII value we have
    and if result lies between 0 and 9, means we got our number
    '''
 
    for i in word:
        val = ord(i) - 48
        if 0 <= val <= 9:
            return True
    return False

def containsNumber2(word):

    val = filter(lambda x: x.isdigit(), word)
    if val:
        return True
    return False


def containsNumber3(word):

    val = re.findall('\d+', word)
    if val:
        return True
    return False
    
if __name__ == '__main__':
    data = sys.argv[1]

    res1 = containsNumber1(data)
    res2 = containsNumber2(data)
    res3 = containsNumber3(data)
 
    if all([res1, res2, res3]):
        print '{} contains number'.format(data)

    else:
        print '{} does not contain number'.format(data)
