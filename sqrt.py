#!/usr/bin/env python
'''
Find square root of a number
http://www.cse.wustl.edu/~kjg/cse131/Notes/SquareRoot/sqrt.html
'''
import sys

def sqrt(num):
    return test(num, 1)

def test(x, g):
    if closeEnough(x/g, g):
        return g
    else:
      return test(x, betterGuess(x, g))

def closeEnough(a, b):

   #a is within 0.1% of b
   #return (abs(a - b) < (b * 0.001))
 
  return (abs(a - b) < .001)

def betterGuess(x, g):

   return ((g + x/g) / 2)



#############################################################
# Using Binary Search - Wont give exact answer


def sqrt(self, x):
    if x < 2:
        return x

    low = 0
    high = x

    while high > low + 1:
        mid = low + (high - low) / 2
        
        div = x / mid

        if mid == div:
            return mid

        elif div > mid:
            low = mid

        else:
            high = mid

    return low






if __name__ == '__main__':
    num = int(sys.argv[1])
 
    print 'Square root of {} is {}'.format(num, sqrt(num))
