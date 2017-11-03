#!/usr/bin/env python
'''
In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. 
Inorder Successor is NULL for the last node in Inoorder traversal.
In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the 
smallest key greater than the key of input node.

'''
# Method1 - Using parent pointers
'''
1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
Go to right subtree and return the node with minimum key value in right subtree.

2) If right sbtree of node is NULL, then succ is one of the ancestors. Do following.
Travel up using the parent pointer until you see a node which is left child of it's parent. The parent of such a node is the succ

Since the number of edges followed cannot be more than the tree height, the time
complexity is O(h), where h is the height of the tree.
'''
def inOrderSuccessor(node):
    if not node:
        return

    if node.right:
        # Find the leftmost element in n's right subtree
        node = node.right
        
        while node.left:
            node = node.left

        return node

    else:
        # Find the first parent whose left child contains n
        while node.parent and node.parent.right == node:
            node = node.parent

        # Return nullptr means n does not have successor
        return node.parent


############################################################################
# Method2: Search from root
'''
1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
Go to right subtree and return the node with minimum key value in right subtree.

2) If right sbtree of node is NULL, then start from root and us search like technique. Do following.
Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.
'''
def inOrderSuccessor_2(root, node):
    if not root:
        return

    if node.right:
        node = node.right
        while node.left:
            node = node.left

        return node


    else:
        succ = None

        # Start from root and search for successor down the tree
        while root:
            if node.data > root.data:
                root = root.right
                
            elif node.data < root.data:
                succ = root
                root = root.left
            else:
                break

        return succ
                















