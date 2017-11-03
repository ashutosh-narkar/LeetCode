#!/usr/bin/env python
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
import string


def convertToTitle(num):
    '''
    This is basically converting integer to  base 26.
    We can use a stack , which means no need to reverse string. Refer int_to_any_base 
    '''
 
    if num == 0:
        return ''

    chars = string.ascii_uppercase
    result = ''
    
    # pay attention to num-1 since indexes begin from 0 
    while num > 0:
        result += chars[(num -1) % 26]
        num = (num - 1) /26
    

    return result[::-1]

        
##########################################################################################
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
def titleToNumber(s):
    '''
    this is converting base 26 to base 10
    '''

    if not s:
        return 

    result = 0


    # We substract from 'ord('A') - 1'. If we dont put the '-1', then titleToNumber('A') = 0, which is wrong 
    for i in range(len(s)):
        result += (ord(s[i]) - (ord('A') - 1)) * (26 ** (len(s) -i -1))
        

    return result



#################################### Simpler Math 
def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0
    
    result = 0
    for ch in s:
        result *= 26
        result += ord(ch) - ord('A') + 1     # +1 is added because titleToNumber(A) would be 0
    return result


