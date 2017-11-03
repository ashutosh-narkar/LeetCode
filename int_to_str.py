#!/usr/bin/env/python

'''
Convert integer to str
'''

import sys


# Similar to excel_sheet
def intToStr2(number):
    if number == 0:
        return '0'

    isNegative = False

    if number < 0:
        number = -number
        isNegative = True

    result = ''

    while number > 0:
        ch = chr(number % 10 + ord('0'))
        result += ch
        number /= 10

    result = result[::-1]

    if isNegative:
        result = '-' + result

    return result


def intToStr(number):
    if number == 0:
        return '0'

    isNegative = False

    if number < 0:
        number = -number
        isNegative = True

    rem_list = []

    while number > 0:
        rem = number % 10
        rem_list.append(rem)
        number /= 10

    result = ''
    while rem_list:
        result += chr(rem_list.pop() + 48)

    if isNegative:
        result = '-' + result

    return result


if __name__ == '__main__':
    input  = int(sys.argv[1])
    print 'Int {} to Str {}'.format(input, intToStr(input))
    print 'Int {} to Str {}'.format(input, intToStr2(input))
