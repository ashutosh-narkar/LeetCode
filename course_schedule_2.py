#!/usr/bin/env python
'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0. 
So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
'''

# Method1: Using DFS. See http://en.wikipedia.org/wiki/Topological_sorting
# Each node 'n' gets prepended to the output list 'L' only after considering all other nodes which depend on 'n' (all descendants of n in the graph). 
# Specifically, when the algorithm adds node 'n', we are guaranteed that all nodes which depend on n are already in the output list L: 
# they were added to L either by the recursive call to dfs() which ended before the call to visit n, or by a call to dfs() which 
# started even before the call to visit n. 
# Since each edge and node is visited once, the algorithm runs in linear time.


def findOrder(numCourses, prerequisites):

    # create the graph (graph can also be represented as dict)
    graph = [[] for _ in range(numCourses)]         # DO NOT USE graph = [[]] * numCourses. Since all lists will point to same object

    # mark all nodes as unvisited
    visited = [0] * numCourses

    for u, v in prerequisites:
        graph[u].append(v)

    result = []

    for i in range(numCourses):
        if not dfs(graph, visited, i, result):
            return []

    return result



def dfs(graph, start, visited, result):


    # cycle in graph
    if visited[start] == -1:
        return False

    if visited[start] == 1:
        return True

    # mark node as "being" visited
    visited[start] = -1
    for neigh in graph[start]:
        if not dfs(graph, neigh, visited, result):
            return False

    # mark node as visited
    visited[start] = 1
    result.append(start)
    return True




################################################################################


# Method2: Using BFS. Runtime O(V + E)

def findOrder(numCourses, prerequisites):

    # create the graph (graph can also be represented as dict)
    graph = [[] for _ in range(numCourses)]

    
    # maintain indegree of nodes
    indegree = [0] * numCourses 


    for course, prereq in prerequisites:
        graph[course].append(prereq)

        # update the in-degree
        indegree[prereq] += 1
        

    # stores nodes with indegree 0. These are the "start nodes"
    # At least one such node must exist in a non-empty acyclic graph
    stack = [i for i in range(numCourses) if indegree[i] == 0]
    
    result = []
    while stack:
        course = stack.pop()
        result.append(course)

        for neigh in graph[course]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                stack.append(neigh)

    if len(result) != numCourses:
        return []

    result.reverse()
    return result







