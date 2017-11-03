#!/usr/bin/env python
"""
Given an array of numbers, return true if given array can represent preorder traversal
of a Binary Search Tree, else return false. Expected time complexity is O(n).


Solution:
1) Create an empty stack.
2) Initialize root as INT_MIN.
3) Do following for every element pre[i]
     a) If pre[i] is smaller than current root, return false.
     b) Keep removing elements from stack while pre[i] is greater
        then stack top. Make the last removed item as new root (to
        be compared next).
        At this point, pre[i] is greater than the removed root
        (That is why if we see a smaller element in step a), we
        return false)
     c) push pre[i] to stack (All elements in stack are in decreasing
        order)

"""


def verifyPreorder(preorder):
    if not preorder:
        return False

    # Initialize current root as minimum possible value
    root = float('-inf')
    stack = []

    for node in preorder:

        # If we find a node who is on the right side
        # and smaller than root, return False
        if node < root:
            return False

        # If value(pre[i]) is in right subtree of stack top,
        # Keep removing items smaller than value
        # and make the last removed items as new root
        while stack and node > stack[-1]:
            root = stack.pop()

        # At this point either stack is empty or value
        # is smaller than root, push value
        stack.append(node)

    return True


if __name__=='__main__':
    print verifyPreorder([2, 4, 3])  # True

    print verifyPreorder([2, 4, 1])  # False

    print verifyPreorder([40, 30, 35, 80, 100])  # True

    print verifyPreorder([40, 30, 35, 20, 80, 100])  # False

