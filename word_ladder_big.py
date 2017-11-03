#!/usr/bin/env python
'''
Words Ladder Problem:
FOOL -> POOL -> POLL -> POLE -> PALE -> SALE -> SAGE

Transform one word into another by changing one character at a time. Each
intermediate word is a legit word
'''
from collections import deque


list_of_words = ['fool', 'foul', 'foil', 'fail', 'fall', 'pall',
                 'poll', 'pool', 'cool', 'pole', 'pope', 'pale',
                 'sale', 'page', 'sage']

def buildGraph():
    '''
    Create an adjacency list representation of the graph.
    The key will be every word in list of words, and value 
    will be a list of words with an edit distance of 1 from the key 
    
    To find all words at edit distance 1, create a dict with key
    equal to word with '_' in a possible locations.
    eg 'pope' would result in keys '_ope', 'p_pe', 'po_e', 'pop_'

    Value would be list of words that match this pattern.
    eg .d['_ope'] = ['pope', 'rope', 'nope', 'hope']

    '''
    d  = {}
    for word in list_of_words:
        for i  in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:] 
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word] 


    graph = {}
    # add vertices and edges for words in the same bucket   
    for pattern, words in  d.items():
        for word1 in words:
            for  word2 in words:
                if word1 != word2:
                    if word1 not in graph:
                        graph[word1] = [word2]
                    else:
                        graph[word1].append(word2)


    return graph
              

def bfs(graph, start):
    '''
    Find the shortest path from start node to
    other nodes in the graph
    '''
    q = deque()
    q.append(start)
 
    visited = []
    visited.append(start)


    distance = {}
    distance[start] = 0   # dist of start node from itself

    pred = {}
    pred[start] = None    # no predecesor to start node


    while q:
        node =  q.popleft()

        for neigh in graph[node]:
            if neigh not in  visited:
                visited.append(neigh)
                q.append(neigh)
 
                distance[neigh] = distance[node] + 1
                pred[neigh] = node

    return (visited, pred)
    

def find_path(pred_info, start, end):
    '''
    given the predecessor info find the path from
    the start node to end node
    '''
    path = []

    node = end
    while node:
        path.append(node)
        node = pred_info[node]

    # since we go from end to start
    path.reverse()

    return path
   

if __name__ == '__main__':
    graph = buildGraph()
    visited_nodes, pred_info = bfs(graph, 'fool')

    if 'sage' not in visited_nodes:
        raise ValueError('cannot reach "sage" from "fool"')


    path = find_path(pred_info, 'fool', 'sage')
    print path




