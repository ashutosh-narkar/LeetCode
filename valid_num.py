#!/usr/bin/env python
'''
Validate if a given string is numeric.

Some examples:
"0" -> true
" 0.1 " -> true
"abc" -> false
"1 a" -> false
"2e10" -> true

'''
import sys

def isNumber(s):
  
        # remove whitespaces from either ends
        s = s.strip()

        n = len(s)

        if not s:
            return False

        i = 0
        dotFlag = False
        EFlag = False
        hasDigit = False
        hasSign = False


        while i < n:

            # if current char is a digit
            # this also implies number is positive
            if s[i].isdigit():
                i += 1
                hasDigit = True
                hasSign = True

            # if current char is '.'
            # this also implies number is positive
            elif not dotFlag and s[i]=='.':
                i += 1

                dotFlag = True
                hasSign = True

            # if current char is 'e' or 'E'
            # prev char should be a digit
            elif hasDigit and not EFlag and (s[i] == 'e' or s[i] == 'E'):

                i += 1

                # set the dotFlag. After an 'e', we shud not have any '.' eg. 6e6.5 => false
                dotFlag = True

                EFlag = True
 
                # we need to reset these 2 flags because, 'e' is followed by a sign and digits
                hasDigit = False
                hasSign = False

            # if current char is a sign
            # this implies either number is negative or this is the sign after 'e'/'E'
            elif not hasDigit and not hasSign and (s[i]=='+' or s[i]=='-'):

                i += 1
                hasSign = True

            else:

                return False

        if hasDigit:
            return True

        else:
            return False

if __name__  == '__main__':
    print isNumber(sys.argv[1])















