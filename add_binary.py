#!/usr/bin/env python
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Idea:
1. Check the length of each string and add "0" to the shorter one.
2. Sum up the two strings, using a "carry" variable to store the carry. 

'''
def addBinary(a, b):

    # make strings equal
    if len(a) > len(b):
        b = b.rjust(len(a), '0')

    else:
        a =a.rjust(len(b), '0')

    a = list(a)
    b = list(b)

    carry = '0'
    
    for i in reversed(range(len(a))):

        # case1
        if a[i] == '0' and b[i] == '0':
            a[i] = carry
            carry = '0'

        # case2
        elif a[i] == '1' and b[i] == '0':
            if carry == '1':
                a[i] = '0'

        # case 3
        elif a[i] == '0' and b[i] == '1':
            if carry == '1':
                a[i] = '0'
            else:
                a[i] = '1'
  
        # case 4
        elif a[i] == '1' and b[i] == '1':
            if carry == '1':
                a[i] = '1'

            else:
                a[i] = '0'
                carry = '1'

    # final carry
    if carry == '1':
        a.insert(0, '1')

    return ''.join(a)


if __name__  == '__main__':
    print addBinary('11', '1')








 
