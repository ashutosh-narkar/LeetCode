#!/usr/bin/env python
"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who
departs from JFK. Thus, the itinerary must begin with JFK.

Note:
1. If there are multiple valid itineraries, you should return the itinerary that has the smallest
   lexical order when read as a single string.
   For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

2. All airports are represented by three capital letters (IATA code).

3. You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

Solution:
All the airports are vertices and tickets are directed edges. Then all these tickets form a directed graph.

The graph must be Eulerian since we know that a Eulerian path exists.
(In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph which visits every edge exactly once)

Thus, start from "JFK", we can apply the Hierholzer's algorithm to find a Eulerian path
in the graph which is a valid reconstruction.

Since the problem asks for lexical order smallest solution, we can put the neighbors in a Min-Heap.
In this way, we always visit the smallest possible neighbor first in our trip.
"""
from heapq import heappush, heappop


class Solution(object):
    def findItinerary(tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []

        flights = {}   # source_airport > min_heap

        for ticket in tickets:
            if ticket[0] not in flights:
                min_heap = []
                flights[ticket[0]] = min_heap

            heappush(flights[ticket[0]], ticket[1])    # push destination airport on min-heap

        result = []
        dfs(result, flights, "JFK")
        return result[::-1]       # reverse the result as "JFK" will get added last in the recursion


def dfs(result, flights, start):
    heap = flights.get(start, [])

    while heap:
        destination = heappop(heap)
        dfs(result, flights, destination)

    result.append(start)