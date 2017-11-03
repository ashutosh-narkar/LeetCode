'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

Method1 - Using DFS
1. if node v has not been visited, then mark it as 0.
2. if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a ring.
3. if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.


Method2: Using BFS. See http://en.wikipedia.org/wiki/Topological_sorting

'''

# Method1: Using DFS
def canFinish(numCourses, prerequisites):

    # create the graph (graph can also be represented as dict)
    graph = [[] for _ in range(numCourses)]         # DO NOT USE graph = [[]] * numCourses. Since all lists will point to same object

    # mark all nodes as unvisited
    visited = [0] * numCourses

    for u, v in prerequisites:
        graph[u].append(v)

    for i in range(numCourses):
        if not dfs(graph, i, visited):
            return False

    return True


def dfs(graph, start, visited):

    # cycle in graph
    if visited[start] == -1:
        return False

    if visited[start] == 1:
        return True

    # mark node as "being" visited
    visited[start] = -1
    for neigh in graph[start]:
        if not dfs(graph, neigh, visited):
            return False

    # mark node as visited
    visited[start] = 1
    return True




####################################################################
# Method2: Using BFS


def canFinish(numCourses, prerequisites):

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

    return len(result) == numCourses


