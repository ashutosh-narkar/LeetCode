#!/usr/bin/env python
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

'''


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    sign = '+'
    num = 0
    stack = []

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + ord(ch) - ord('0')

        # This condition "i == len(s) - 1" is useful when len(s) = 1
        if (not ch.isdigit and not ch.isspace()) or i == len(s) - 1:
            if sign == '+':
                stack.append(num)

            elif sign == '-':
                stack.append(-num)

            # since we are going to add the stack elements, we pop and multiply
            elif sign == '*':
                stack.append(stack.pop() * num)

            # since we are going to add the stack elements, we pop and divide
            elif sign == '/':
                stack.append(stack.pop() / num)

            num = 0
            sign = ch

    return sum(stack)

if __name__=='__main__':
    input = '1 + 1'
    print(calculate(input))