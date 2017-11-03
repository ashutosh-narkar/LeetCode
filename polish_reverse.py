#!/usr/bin/env python
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

# Solution 1
# We can loop through each element in the given array.
# When it is a number, push it to the stack.
# When it is an operator, pop two numbers from the stack, do the calculation, and push back the result

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """

    stack = []

    for token in tokens:
        if token not in ['+', '-', '*', '/']:          # can't use token.isdigit() as '-5'.isdigit() = False
            stack.append(int(token))

        else:
            num1, num2 = stack.pop(), stack.pop()

            if token == '+':
                stack.append(num2 + num1)

            elif token == '-':
                stack.append(num2 - num1)

            elif token == '*':
                stack.append(num2 * num1)

            else:
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in
                # Leetcode it should return 0
                if num2 * num1 < 0 and num2 % num1 != 0:
                    stack.append(num2 / num1 + 1)
                else:
                    stack.append(num2 / num1)

    return stack.pop()





# Solution 2
import operator
import re

def evalRPN(tokens):
    if not tokens:
	    return -1

    operators = {}
    operators['+'] = operator.add
    operators['-'] = operator.sub
    operators['*'] = operator.mul
    operators['/'] = operator.truediv


    stack = []

    for char in tokens:
        if re.findall('\d', char):
            stack.append(char)
        if char in ('+', '-', '*', '/'):
	        fn = operators[char]
	        num1 = stack.pop()
	        num2 = stack.pop()
	        result = int(fn(int(num2), int(num1)))
	        stack.append(str(result))

    return int(stack.pop())

if __name__ == '__main__':
    input = ['5', '6', '2', '+', '*', '12', '4', '/', '-']
    print evalRPN(input)

