#!/usr/bin/env python
'''
Determine whether an integer is a palindrome. Do this without extra space.
Assume negative integers as non-palindromes.
'''
import sys

def isPalindrome(x):
  
  if (x < 0):
    return False

  div = 1
  while (x / div >= 10):
    div *= 10

  while (x != 0):
    l = x / div
    r = x % 10
    if (l != r):
        return False
    x = (x % div) / 10
    div /= 100

  return True


if __name__ == '__main__':
    num = int(sys.argv[1])
    if isPalindrome(num):
        print '{} is a palindrome'.format(num)

    else:
        print '{} is not a palindrome'.format(num)
