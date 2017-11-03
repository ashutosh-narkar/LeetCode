#!/usr/bin/env python
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
def sumNumbers(root):

    if not root:
        return 0

    result = []
    traverse(root, result)

    return sum(result)


def traverse(root, result, val=0):

    if not root:
        return

    val = val * 10 + root.val

    if not root.left and not root.right:
        result.append(val)

    traverse(root.left, result, val)
    traverse(root.right, result, val)
