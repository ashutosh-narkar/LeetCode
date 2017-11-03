#!/usr/bin/env python
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and
node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''


# Time complexity : O(m*n) . In worst case(skewed tree) traverse function takes O(m*n) time.

# Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in s.

def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    # if the left tree is empty, then right tree can't be a subtree
    if not s:
        return False

    # we have 3 options
    # 1. Subtree starts from the root of the first tree
    # 2. Subtree starts from the left child of the first tree. So treat the left child as root and compare with t
    # 3. Subtree starts from the right child of the first tree. So treat the right child as root and compare with t

    # This is a pre-order traversal of s

    if equals(s, t):
        return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)


def equals(t1, t2):
    if not t1 and not t2:
        return True

    if not t1 or not t2:
        return False

    if t1.val != t2.val:
        return False

    return equals(t1.left, t2.left) and equals(t1.right, t2.right)