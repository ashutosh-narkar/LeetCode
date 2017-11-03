#!/usr/bin/env python
"""
BFS

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
"""
from collections import deque


def bfs(graph, start):

    # mark all nodes as unvisited
    visited = [False] * len(graph)

    queue = deque()

    queue.append(start)
    visited[start] = True    # we can also use a set for the visited nodes

    result = []

    while queue:
        node = queue.popleft()

        result.append(node)

        # Get all adjacent vertices of the dequeued
        # vertex 'node'. If a adjacent has not been visited,
        # then mark it visited and enqueue it
        for neigh in graph[node]:
            if not visited[neigh]:
                queue.append(neigh)
                visited[neigh] = True

    return result

if __name__ == '__main__':
    nodes = 4
    graph = [[] for _ in range(nodes)]
    graph[0].append(1)
    graph[0].append(2)

    graph[1].append(0)
    graph[1].append(2)

    graph[2].append(0)
    graph[2].append(1)
    graph[2].append(3)

    graph[3].append(2)

    print bfs(graph, 2)


# Note that the above code traverses only the vertices reachable from a given source vertex.
# All the vertices may not be reachable from a given vertex (example Disconnected graph).
# To print all the vertices, we can call BFS starting from all the graph nodes one by one
