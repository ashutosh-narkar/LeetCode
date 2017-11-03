#!/usr/bin/env python
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''


# Solution 1: Similar to height_tree.py and binary_tree_right_side.py
from collections import deque


def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    queue = deque()
    queue.append(root)

    curr = 1
    next = 0

    temp = []
    result = []

    while queue:
        node = queue.popleft()

        curr -= 1
        temp.append(node.val)

        if node.left:
            next += 1
            queue.append(node.left)

        if node.right:
            next += 1
            queue.append(node.right)

        if curr == 0:
            result.append(temp)
            temp = []

            curr = next
            next = 0

    return result




# Solution: 2
# 1) Print the nodes at the current level
# 2) Collect children of nodes at current level
# 3) Update the level list with nodes to be processed in the next iteration
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    result = []
    level = [root]

    while level:

        # 1. Print the nodes at the current level
        result.append([node.val for node in level])
        # temp = []
        # for node in level:
        #    temp.append(node.val)

        # result.append(temp)


        # 2. Collect children of nodes at current level
        LRpair = [(node.left, node.right) for node in level]

        # 3. Update the level list with nodes to be processed in the next iteration
        level = []
        for pair in LRpair:
            for node in pair:
                if node:
                    level.append(node)

    return result