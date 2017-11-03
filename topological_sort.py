#!/usr/bin/env python
'''
Topological Sort using DFS
Assume graph is a Directed Acyclic Graph

Runtime O(m+n)

Given a set of vertices and a set of directed edges between vertices, Topological Sort (i.e. toposort) is to 
produce a linear ordering of vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
Toposort only works in Directed Acyclic Graphs (DAG). The most common use case is job scheduling.

Alternate Question:
Given an instance of the task scheduling problem, compute the least
amount of time in which all the tasks can be performed, assuming an unlimited number of
servers. Explicitly check that the system is feasible.

-> The system is infeasible iff a cycle is present in the derived graph
Since the number of servers is unlimited, Ti can be completed ti time after all the
tasks it depends on have completed. Therefore, we can compute the soonest each
task can complete by processing tasks in topological order, starting from the tasks
that depend on no other tasks. If no such task exists, system is infeasible. There is a cycle.
'''

time = 1
finish_times = {}

def dfs(graph, start, visited):
    if not start:
        return
    visited.append(start)
    for neigh in graph[start]:
        if neigh not in visited:
            dfs(graph, neigh, visited)

    # set node finish time after all its neighbours are visited
    global finish_times, time
    finish_times[start] = time
    time += 1


def dfs_loop(graph):
    unvisited = set(graph.keys())
    visited = []

    while unvisited:
        vertex = unvisited.pop()
        dfs(graph, vertex, visited)
        unvisited -= set(visited)


if __name__ == '__main__':

    graph = {7: [11, 8],
             5: [11],
             3: [8, 10],
             11: [2,9,10],
             8: [9],
             10: [],
              2: [],
              9: []}


    dfs_loop(graph)
    finish_times_sorted = sorted(finish_times.items(), key=lambda x: x[1], reverse=True)
    
    print 'Topological Sort is'
    for node, time in finish_times_sorted:
        print node
