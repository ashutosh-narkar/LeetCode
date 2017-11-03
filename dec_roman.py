#!/usr/bin/env python
'''
Dec to roman conversion and vice-versa
'''

import sys

coding = zip(
    [1000,900,500,400,100,90,50,40,10,9,5,4,1],
    ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
)

romanNumeralMap = [(roman, num) for num, roman in coding]

def decToRoman(num):
    """convert integer to Roman numeral using DP"""

    if not num or not isinstance(num, int):
        raise ValueError('Invalid Input')

    num_count = []
    dec_roman = []
    for i in range(num + 1):
        minNumerals = i
        numUsed = 'I'

        possible_values = [(num, roman) for num, roman in coding  if num <=i]
       
        for num, roman in possible_values:
            numNeeded = num_count[i - num] + 1
            if numNeeded < minNumerals:
                minNumerals = numNeeded
                numUsed = roman

        num_count.insert(i, minNumerals)
        dec_roman.insert(i, numUsed)
    return (num_count, dec_roman)


def _print_numerals_used(num, romanlist):

    result = ''
    while num > 0:
        symbol = romanlist[num]
        result += symbol
        decvalue = [_num for _num, _roman in coding if _roman == symbol][0]
        num -= decvalue
    return result
     
def romanToDec(s):
    """convert Roman numeral to integer"""
   
    if not s:
        raise ValueError('Invalid Input')
    
    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
    

def decToRoman_2(n):
    """convert integer to Roman numeral"""

    if not n or not isinstance(n, int):
        raise ValueError('Invalid Input')

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

if __name__ == '__main__':
    
    # decimal to roman 
    _input = int(sys.argv[1])
    num_numerals, used_numerals = decToRoman(_input)
    roman = _print_numerals_used(_input, used_numerals)
    print 'Method 1: Dec {} to Roman {}'.format(_input, roman)

    print 'Method 2: Dec {} to Roman {}'.format(_input, decToRoman_2(_input))

    # decimal to roman
    print 'Roman {} to Decimal {}'.format(roman, romanToDec(roman))

