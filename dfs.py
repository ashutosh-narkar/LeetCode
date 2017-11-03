#!/usr/bin/env python
'''
DFS
'''


def dfs_rec(graph, start, visited, result):

    # Mark the current node as visited
    visited[start] = True
    result.append(start)

    for neigh in graph[start]:
        if not visited[start]:
            dfs_rec(graph, neigh, visited, result)


def dfs_iter(graph, start):

    visited= []
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited
    

if __name__ == '__main__':

    nodes = 8
    graph = [[] for _ in range(nodes)]
    graph[0].append(3)
    graph[1].append(3)
    graph[2].append(3)
    graph[3].append(8)
    graph[3].append(5)
    graph[4].append(5)
    graph[5].append(6)
    graph[6].append(7)
    graph[7].append(7)

    result = []
    # Mark all the vertices as not visited
    visited = [False] * nodes

    print "Recursive DFS"
    # Call the recursive helper function to print
    # DFS traversal starting from all vertices one
    # by one
    for node in range(nodes):
        if not visited[node]:
            dfs_rec(graph, node, visited, result)
            print result

    print '\n Iterative DFS'
    print dfs_iter(graph, 2)
