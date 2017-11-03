#!/usr/bin/env python
'''
Evaluate the value of an arithmetic expression in Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
 ("- * / 15 - 7 + 1 1 3 + 2 + 1 1") -> 5
  
'''
import operator
import re

def evalRPN(tokens):
    if not tokens:
        return -1

    tokens = tokens.split()

    operators = {}
    operators['+'] = operator.add
    operators['-'] = operator.sub
    operators['*'] = operator.mul
    operators['/'] = operator.truediv

    stack = []

    for i in range(len(tokens) - 1, -1, -1):
        char = tokens[i]
        if re.findall('\d', char):
            stack.append(char)
        if char in ('+', '-', '*', '/'):
            fn = operators[char]
            num1 = stack.pop()
            num2 = stack.pop()
            result = int(fn(int(num1), int(num2)))
            stack.append(str(result))

    return int(stack.pop())

if __name__ == '__main__':
    input = ("- * / 15 - 7 + 1 1 3 + 2 + 1 1")
    assert evalRPN(input) == 5
    
    input = ("/ - * 2 5 * 1 2 - 11 9")
    assert evalRPN(input) == 4

    print 'Tests passed'
