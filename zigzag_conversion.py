#!/usr/bin/env python
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
def convert(s, nRows):

    if not s:
        return ''

    if nRows == 1:
        return s
        

    y = 0
    flag = True

    result = [''] * nRows      # each list element represents a row of zigzag
    

    # basically we down and then up while filling rows

    for i in range(len(s)):
        result[y] += s[i]
        
        if y == 0:
            flag = True

        elif y == nRows - 1:
            flag = False

        if flag:
            y += 1
        else:
            y -= 1

    return ''.join(result)
