#!/usr/bin/env python
'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

AND

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
# Recursive 1
'''
Complexity:
O(n) time
O(logn) space
'''
def maxDepth(root):
    if not root:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1



# Iterative 1
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    nodeStack = []
    nodeStack.append(root)

    maxDepth = 0
    depthStack = [1]  # at root , depth is 1

    while stack:
        node = nodeStack.pop()
        depth = depthStack.pop()

        maxDepth = maxDepth if maxDepth > depth else depth

        if node.left:
            nodeStack.append(node.left)
            depthStack.append(depth + 1)

        if node.right:
            nodeStack.append(node.right)
            depthStack.append(depth + 1)

    return maxDepth






# Recursive 2
def maxDepth(root):
    if not root:
        return 0
    return getHeight(root)
        

def getHeight(root):

    if not root:
        return 0


    left = getHeight(root.left)
    right = getHeight(root.right)

    return max(left, right) + 1



# Using BFS
def maxDepth(self, root):

    if not root:
        return 0

    queue = deque()
    queue.append(root)

    level = 0
    nodes_current, nodes_next = 1, 0 

    while queue:
        node = queue.popleft()
        nodes_current -= 1

        if node.left:
            queue.append(node.left)
            nodes_next += 1

        if node.right:
            queue.append(node.right)
            nodes_next += 1

        # end of level
        if nodes_current == 0:
            level += 1
            nodes_current, nodes_next = nodes_next, 0

    return level


####################################
def minDepth(root):
    if not root:
	    return 0

    return getHeight(root)

        

def getHeight(root):
    if not root:
        return float('inf')

    # leaf node
    if not root.left and not root.right:
        return 1


    left = getHeight(root.left)
    right = getHeight(root.right)

    return min(left, right) + 1


# Using BFS 

from collections import deque
def minDepth(root):
    if not root:
	    return 0

    explored = deque()
    explored.append((root, 1))

    while explored:
	    (node, depth) = explored.popleft()

        # leaf node
	    if not (node.left or node.right):
	        return depth

	    if node.left:
	        explored.append((node.left, depth+1))

	    if node.right:
	        explored.append((node.right, depth+1))





