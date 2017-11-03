#!/usr/bin/env python
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return []

    result = []

    # we need 'n' open and close parens
    backtrace(n, n, result, '')
    return result

# 'open' and 'close' represent the number of '(' and ')' parens we NEED to add
def backtrace(open, close, result, s):

    # to avoid a pattern like '(()))('
    if close < open:
        return

    if open == 0 and close == 0:
        result.append(s)
        return

    if open > 0:
        backtrace(open - 1, close, result, s + '(')

    if close > 0:
        backtrace(open, close - 1, result, s + ')')


if __name__ == '__ main__':
    res  = generateParenthesis(3)
    print res
