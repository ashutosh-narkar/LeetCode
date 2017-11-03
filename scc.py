#!/usr/bin/env python
'''
Kosaraju Algorithm to find Strongly Connected Component (SCC) of a directed graph.
Runtime O(m+n)

Steps:
1) Compute transpose of G
2) Call dfs on the transpose of G and compute finishing times
3) Run dfs on original graph in decreasing order of finishing times(Replace nodes in original nodes by their finishing times)
4) Each tree in the forest computed in step 3 is a strongly connected component.
'''


time = 0
finish_times = {}


def dfs(dgraph, start, visited=[]):
    if not start:
        return 

    visited.append(start)
    for neigh in dgraph[start]:
        if neigh not in visited:
            dfs(dgraph, neigh, visited)

    global finish_times, time
    time += 1
    finish_times[start] = time

    return visited


def dfs_loop_1(graph):

    visited = set()

    # start from highest numbered node
    for node in reversed(graph.keys()):
        if node not in visited:
            res = dfs(graph, node)
            visited.update(set(res))
     

def dfs_loop_2(graph):
    # run dfs in decreasing order of finish times
    # In the original graph, replace node by its finish time
    graph_finish_time = {}
    for node, neighs in graph.items():
        key = finish_times[node]
        val = []
        for neigh in neighs:
            val.append(finish_times[neigh])

        graph_finish_time[key] = val
  
    
    connected_comp = []
    nodes_visited = []
    prev_nodes_visted = []

    # start from highest numbered node
    for node in reversed(graph_finish_time.keys()):
        if node not in nodes_visited:
            dfs(graph_finish_time, node, visited=nodes_visited)
            cc = set(nodes_visited) - set(prev_nodes_visted)            
            connected_comp.append(cc)
            prev_nodes_visted.extend(nodes_visited)


    return connected_comp

   
def transpose_graph(graph):
    graph_transpose = {}

    for node, neighs in graph.items():
        for neigh in neighs:
            if neigh in  graph_transpose:
                graph_transpose[neigh].append(node)

            else:
                graph_transpose[neigh] = [node]


    # add values for missing entries
    for node in graph.keys():
        if node not in graph_transpose:
            graph_transpose[node] = []

    return graph_transpose


if __name__ == '__main__':

    graph = {1: [4],
             2: [8],
             3: [6],
             4: [7],
             5: [2],
             6: [9],
             7: [1],
             8: [5, 6],
             9: [7, 3]}



    # Step 1: Reverse original graph 
    graph_rev = transpose_graph(graph)

    # Step 2: Find finish times in reversed graph
    dfs_loop_1(graph_rev)
     
    # Step 3: Run DFS on orignal graph in decreasing order of finish times
    scc = dfs_loop_2(graph)
    
    print 'SCC {}'.format(scc)


