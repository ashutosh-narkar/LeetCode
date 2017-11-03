#!/usr/bin/env python
'''
Detect cycle in an undirected graph using dfs and no parent pointers
'''
def isCycle(graph):

    if not graph:
        return False

    # mark all nodes as unvisited
    visited = [0] * len(graph)

    for node in range(len(graph)):
        if dfs(graph, node, visited):
            return True

    return False


def dfs(graph, start, visited):

    # cycle in graph
    if visited[start] == -1:
        return True

    # no cycle in graph
    if visited[start] == 1:
        return False

    # mark node as "being" visited
    visited[start] = -1

    for neigh in graph[start]:
        if dfs(graph, neigh, visited):
            return True

    # mark node as visited
    visited[start] = 1
    return False



if __name__ == '__main__':

    graph = [[1, 2, 3], [0, 2],  [0, 1], [0], [3]]

    assert isCycle(graph) == True

    graph = [[1], [2], []]
    assert isCycle(graph) == False
     
    print 'tests passed' 
