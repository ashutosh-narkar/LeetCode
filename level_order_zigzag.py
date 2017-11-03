#!/usr/bin/env python
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Solution 1 : Runtime O(n)

#1) pop from stack "current" and store the node’s value.

#2) Whenever the current level’s order is from left->right, you push the node’s left child,
# then its right child to stack "next".
# Remember a Stack is a Last In First OUT (LIFO) structure,
# so the next time when nodes are popped off nextLevel, it will be in the reverse order.

# 3) On the other hand, when the current level’s order is from right->left,
# you would push the node’s right child first, then its left child.

# 4) Finally, don’t forget to swap those two stacks at the
# end of each level (ie, when currentLevel is empty).


def zigzagLevelOrder_1(root):
	if not root:
		return []

	current, next = [], []
	current.append(root)

	leftToRight = True

	result = []
	temp = []

	while current:

		node = current.pop()
		temp.append(node.val)

		if leftToRight:
			if node.left:
				next.append(node.left)

			if node.right:
				next.append(node.right)

		else:
			if node.right:
				next.append(node.right)

			if node.left:
				next.append(node.left)

		if not current:
			result.append(temp)
			temp = []

			leftToRight = not leftToRight

			current, next = next, current

	return result





"""
Solution 1: Minor change in levelOrder.py
Runtime - O(n^2)
"""


def zigzagLevelOrder_2(root):
	"""
    :type root: TreeNode
    :rtype: List[List[int]]
    """
	if not root:
		return []

	result = []
	level = [root]

	direction = 1

	while level:
		result.append([node.val for node in level][::direction])

		# reverse the direction
		direction *= -1

		LRpair = [(node.left, node.right) for node in level]

		level = []
		for pair in LRpair:
			for node in pair:
				if node:
					level.append(node)

	return result



