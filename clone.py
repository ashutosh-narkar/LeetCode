#!/usr/bin/env python
'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

From the way the Node class is defined, this approach should work for directed graphs as well
'''

# Definition for a undirected graph node

class UndirectedGraphNode:

     def __init__(self, x):
         self.label = x
         self.neighbors = []



from collections import deque

# Using BFS
def cloneGraph(node):

    if not node:
        return

    # add nodes of the original graph to the queue
    queue = deque()
    queue.append(node)

    nodeMap = {}

    # create a new node
    newNode = UndirectedGraphNode(node.label)

    # add nodes of the new graph to the dict. This is similar to "visited" list in BFS
    nodeMap[newNode.label] = newNode

    while queue:
        oldnode = queue.popleft()

        for neigh in oldnode.neighbors:
            if neigh.label not in nodeMap:
                # add nodes from original graph to queue
                queue.append(neigh)

                # add nodes from new graph to dict
                nodeMap[neigh.label] = UndirectedGraphNode(neigh.label)
     
                # update the neighbours of the cloned node
                nodeMap[oldnode.label].neighbors.append(nodeMap[neigh.label])


    return newNode

	
###############################################
# Using DFS
def cloneGraph(node):

    if not node:
        return

    nodeMap = {}
    return dfs(node, nodeMap)


def dfs(oldNode, nodeMap):

    newNode = UndirectedGraphNode(oldNode.label)
    nodeMap[newNode.label] = newNode

    for neigh in oldNode.neighbors:
        if neigh.label not in nodeMap:
            dfs(neigh, nodeMap)

        # update the neighbours of the cloned node
        newNode.neighbors.append(nodeMap[neigh.label])

    return newNode
    
