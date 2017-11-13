#!/usr/bin/env python
"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
from collections import deque


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# Solution1: Constant space
# Idea is to use BFS, but instead of storing each level in the queue,
# we just store the first node of this level because we can utilize the "next" property to traverse the whole level.
# Solution works for ANY Binary Tree


def connect(root):
    if not root:
        return

    prev = root
    current = None

    while prev.left:
        current = prev

        while current:
            current.left.next = current.right

            if current.next:
                current.right.next = current.next.left

            current = current.next

        prev = prev.left

    return


# Solution 2: Uses extra space
# Perform a level order traversal and then connect nodes

def connect(root):

    if not root:
        return

    queue = deque()
    queue.append(root)

    nodes_current = 1
    nodes_next = 0

    result = []
    temp = []

    while queue:
        node = queue.popleft()

        nodes_current -= 1
        temp.append(node)

        if node.left:
            queue.append(node.left)
            nodes_next += 1

        if node.right:
            queue.append(node.right)
            nodes_next += 1

        if nodes_current == 0:
            result.append(temp)
            temp = []

            nodes_current, nodes_next = nodes_next, 0

    for item in result:
        if len(item) > 1:
            for i in range(len(item) - 1):
                item[i].next = item[i + 1]