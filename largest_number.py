#!/usr/bin/env python
'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
def largestNumber(num):
    if not num:
        return ''

    num = map(str, num)
    
    # sort the list of strings in descending order
    num.sort(cmp=compare, reverse=True)
    return ''.join(num).lstrip('0') or '0'   # if we simply return ''.join(num), we will get '00' for ['0', '0']
    

def compare(a, b):
    '''
    eg. (a="2",b="11") 'a' is bigger than 'b' because "211" >"112"
    '''
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0


if __name__ == '__main__':
    input = [3, 30, 34, 5, 9]

    print 'Largest Number that can be formed with {} is {}'.format(input, largestNumber(input))
