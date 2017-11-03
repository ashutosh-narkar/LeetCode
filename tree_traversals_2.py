#!/usr/bin/env python
'''
Given a binary tree, return the inorder traversal of its nodes' values using iteration.

Solution:
In the loop: If we get a node with flag false, we add children in correct order and set them to false, because they have to be processed (for their children). 
             And we set flag of current node to true.

If we get node with flag set to true we simply add it to our result.

'''

# Recursive
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    recursive_inorder(root, result)
    return result


def recursive_inorder(root, result):
    if not root:
        return

    recursive_inorder(root.left, result)
    result.append(root.val)
    recursive_inorder(root.right, result)


# Iterative

def inorderTraversal(root):

    if not root:
	    return []


    stack = []
    stack.append((False, root))

    result = []

    while stack:
        flag, node = stack.pop()

        if node:
            if not flag:
                # add in reverse order so that they are popped correctly
                stack.append((False, node.right))
                stack.append((True, node))
                stack.append((False, node.left))

            else:
                result.append(node.val)

    return result



###########################################################
def preorderTraversal(root):

    if not root:
	return []

    stack = []
    stack.append((False, root))

    result = []

    while stack:
        flag, node = stack.pop()

        if node:
            if not flag:
                stack.append((False, node.right))
                stack.append((False, node.left))
                stack.append((True, node))

            else:
                result.append(node.val)

    return result


###########################################################
def postorderTraversal(root):

    if not root:
	return []

    stack = []
    stack.append((False, root))

    result = []

    while stack:
        flag, node = stack.pop()

        if node:
            if not flag:
                stack.append((True, node))
                stack.append((False, node.right))
                stack.append((False, node.left))
            
                else:
                    result.append(node.val)

    return result
