#!/usr/bin/env python
"""
Given a Tree where every node contains variable number of children, convert the tree to its mirror

Example:

            10
    2    34     56     100
         1           7  8  9

             TO

             10
    100       56    34    2
9    8   7           1

"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def mirror_tree(root):
    if not root:
        return

    #  Number of children of root
    n = len(root.children)

    # If number of child is less than 2 i.e.
    # 0 or 1 we don't need to do anything
    if n < 2:
        return

    # Calling mirror function for each child
    for i in range(n):
        mirror_tree(root.children[i])

    # Reverse variable sized array of child pointers
    root.children.reverse()


def print_level_order(root):
    if not root:
        return

    q = deque()
    q.append(root)
    curr_level = 1
    next_level = 0

    temp = []

    while q:
        node = q.popleft()
        curr_level -= 1

        temp.append(node.val)

        for child in node.children:
            next_level += 1
            q.append(child)

        if curr_level == 0:
            print list(temp)
            temp = []
            curr_level = next_level
            next_level = 0

if __name__ == '__main__':
    root = Node(10)
    child1 = Node(2)
    child2 = Node(34)
    child3 = Node(56)
    child4 = Node(100)

    root.children = [child1, child2, child3, child4]
    child2.children = [Node(1)]
    child4.children = [Node(7), Node(8), Node(9)]

    print "Level order traversal Before Mirroring"
    print_level_order(root)

    mirror_tree(root)
    print "\nLevel order traversal After Mirroring"
    print_level_order(root)
