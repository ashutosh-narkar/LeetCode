#!/usr/bin/env python
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

"""

from collections import deque


def isSymmetric_iter(root):

    if not root:
        return True

    queue = deque()
    queue.append((root.left, root.right))

    while queue:
        node1, node2 = queue.popleft()

        if not node1 and not node2:
            continue

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        # node1.left and node2.right are symmetric nodes in structure
        # node1.right and node2.left are symmetric nodes in structure
        queue.append((node1.left, node2.right))
        queue.append((node1.right, node2.left))

    return True     


# Recursive Solution
def isSymmetric_rec(root):

    if not root:
        return True

    return _isSymmetric(root.left, root.right)


def _isSymmetric(left, right):

    # both empty
    if not left and not right:
        return True

    # one is empty
    if not left or not right:
        return False

    # unequal val
    if left.val != right.val:
        return False

    return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)   



############ Iterrative W/O queue
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
                                            
    if not root:
        return True
                                                                        
    stack = [[root.left, root.right]]

    while len(stack) > 0:
        left,right = stack.pop()
                                                                                                    
        # both empty
        if not left and not right:
            continue
                    
        # one of them is empty
        if not left or not right:
            return False
                                                                                                                                                                        
        # unequal values                                                                                                                                                                  if left.val != right.val:   
            return False

        stack.append([left.left, right.right])
        stack.append([left.right, right.left])


    return True



