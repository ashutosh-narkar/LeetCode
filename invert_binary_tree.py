#!/usr/bin/env python
'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

TO

     4
   /   \
  7     2
 / \   / \
9   6 3   1


'''

# Solution 1: Recursive
'''
Complexity Analysis

Since each node in the tree is visited only once, the time complexity is O(n), where n is the number of nodes in the tree. 
We cannot do better than that, since at the very least we have to visit each node to invert it.

Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree.
Because h E O(n), the space complexity is O(n).
'''
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return

    nodeLeft = invertTree(root.left)
    nodeRight = invertTree(root.right)

    root.left = nodeRight
    root.right = nodeLeft

    return root


# Solution 2: Iterative
# Time:  O(n)
# Space: O(h)
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return

    nodeStack = []
    nodeStack.append(root)

    while nodeStack:
        node = nodeStack.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            nodeStack.append(node.left)

        if node.right:
            nodeStack.append(node.right)

    return root
