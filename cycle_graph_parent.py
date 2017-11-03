#!/usr/bin/env python
'''
Detect cycle in an undirected graph using parent pointers
'''

def isCycle(graph, start, visited=[], parent=None):
    if not start:
        return

    print visited 
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            isCycle(graph, node, visited=visited, parent=start)


        # If an adjacent is visited and not parent of current vertex,
        # then there is a cycle.
        else:
            if node != parent:
                return True
    return False




if __name__ == '__main__':
    graph = {'0': ['1', '2', '3'],
             '1': ['0', '2'],
             '2': ['0', '1'],
             '3': ['0'],
             '4': ['3']}

    assert isCycle(graph, '0') == True

    graph = {'0': ['1'],
             '1': ['2'],
             '2': []}

    assert isCycle(graph, '0') == False
     
    print 'tests passed' 
