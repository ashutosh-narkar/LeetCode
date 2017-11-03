#!/usr/bin/env python
'''
Evaluate an expression represented by a String. The expression uses the inflix notation.
Expression can contain parentheses, you can assume parentheses are well-matched. 

eg.  5 * ( 6 + 2 ) - 12 / 4

Step1: Convert inflix notation to postfix(reverse polish) notation
        5 6 2 + * 12 4 / -

Reference - http://faculty.cs.niu.edu/~hutchins/csci241/eval.htm
'''
import re
import operator

def convertInflixToPostfix(expression):

    # can be any value but order is important
    precedence = {}
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['^'] = 4
    

    postfix = []
    operators = []

    # remove spaces
    expression = expression.split()

    for char in expression:

        # operand
        if re.findall('\d', char):
            postfix.append(char)

        # left paren
        if char == '(':
            operators.append(char)

        # right paren
        if char == ')':
            # pop till left paren not found
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())

            # if stack is empty, this means no left paren and hence the inflix expression is unbalanced

            # pop left paren 
            if operators:
                operators.pop()

        # operator found
        if char in precedence:
            # if stack empty or element at stack top is a left paren
            if not operators or operators[-1] == '(':
                operators.append(char)

            else:
                # while the stack is not empty AND the top of the stack 
                # is not a left parenthesis AND precedence of the                  
                # operator <= precedence of the top of the stack)
                # Pop the stack and add the top value to postfix
                while operators and operators[-1] != '(' and precedence[char] <= precedence[operators[-1]]:
                    postfix.append(operators.pop())

                # push current operator
                operators.append(char)


        
    # pop the operators stack and add to postfix
    # if the operatots stack contains a 'left paren', then inflix expression is unbalanced
    while operators:
        postfix.append(operators.pop())

    # add spaces
    return ' '.join(postfix)

def evalPostfix(exp):

    operators = {}
    operators['+'] = operator.add
    operators['-'] = operator.sub
    operators['*'] = operator.mul
    operators['/'] = operator.truediv
    operators['^'] = operator.pow

    # remove spaces
    exp = exp.split()

    result = []

    for char in exp:
        if re.findall('\d', char):
            result.append(char)

        elif char in operators:
            num1 = int(result.pop()) 
            num2 = int(result.pop())
            fn = operators[char]
            res = int(fn(num2, num1))  # convert answer to int
            result.append(str(res))


    return int(result.pop())



def evalExpression(exp):
    if not exp:
        return 0

    # step0: check for balanced parens

    # step1: convert inflix to postfix
    postfix_exp = convertInflixToPostfix(exp)

    # step2: eval postfix exp
    return evalPostfix(postfix_exp)



if __name__ == '__main__':
    input = '5 * ( 6 + 2 ) - 12 / 4' 
    assert evalExpression(input) == 37


    input = '10 + 2 * 6' 
    assert evalExpression(input) == 22


    input = '100 * 2 + 12' 
    assert evalExpression(input) == 212


    input = '100 * ( 2 + 12 )' 
    assert evalExpression(input) == 1400


    input = '100 * ( 2 + 12 ) / 14' 
    assert evalExpression(input) == 100


    input = '10 * ( 2 + 3 ) ^ 3' 
    assert evalExpression(input) == 1250


    print 'Tests passed'
