#!/usr/bin/env python
'''
Longest Valid Parenthesis

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

import sys


def longestValidParentheses(s):

    if not s:
        return 0

    stack = []
    max_length = 0
    start = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)

        else:
            # no '(' to match the ')'
            if not stack:
                start = i + 1
            else:
                stack.pop()
                
                # if after popping, stack becomes empty, store length from the start
                # else calculate length from the most recent '('
                if not stack:
                    max_length = max(max_length, i - start + 1)
                else:
                    max_length = max(max_length, i - stack[-1])

    return max_length
       

if __name__ == '__main__':
    data = sys.argv[1]
    print 'Length of longest valid pare for {} is {}'.format(data, longestValidParentheses(data)) 

        
