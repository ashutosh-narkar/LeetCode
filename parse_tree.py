#!/usr/bin/env python
'''
Build a Parse Tree to evaluate a math expression
http://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html
'''
import operator
from binary_tree import BinaryTree

def buildParseTree(expression):
    explist = expression.split()

    # start a parse tree with a empty root node
    ptree = BinaryTree('')
    
    # maintain a stack to keep track of parent
    pstack = []
 
    pstack.append(ptree)
    current = ptree

    for item in explist:
        if item == '(':
            current.insertLeft('')
            pstack.append(current)
            current = current.getLeft()    

        elif item in ['+', '-', '*', '/']:
            current.setData(item)
            current.insertRight('')
            pstack.append(current) 
            current = current.getRight()

        elif item.isdigit():
            current.setData(int(item))
            current = pstack.pop()

        elif item == ')':
            current = pstack.pop()

        else:
            raise ValueError


    return ptree


def evaluate(parsetree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}



    # a base case for recursive algo that operate on trees
    # is to check for leaf node

    leftchild = parsetree.getLeft()
    rightchild = parsetree.getRight()

    if  leftchild and rightchild:
        fn = opers[parsetree.getData()]
        return fn(evaluate(leftchild), evaluate(rightchild))

    else:
        return parsetree.getData()    


def postordereval(parsetree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    # instead of printing the node value as in postorder traversal, we return value    
    if parsetree:
        res1 = postordereval(parsetree.getLeft())
        res2 = postordereval(parsetree.getRight())
        
        if res1 and res2:
            fn = opers[parsetree.getData()]
            return fn(res1, res2)

        else:
	    return parsetree.getData()

def printexp(parsetree):
    tree = ''
    if parsetree:
        tree = '(' + printexp(parsetree.getLeft())
        tree += str(parsetree.getData())
        tree += printexp(parsetree.getRight()) + ')'

    return tree


if __name__ == '__main__':
    pt = buildParseTree("( ( 8 * 2 ) * ( 5 - 2 ) )")
    res = postordereval(pt)
    print 'result {}'.format(res)
    print printexp(pt)



