#!/usr/bin/env python
"""
Given a square chessboard of N x N size, the position of Knight and position of a target is given.
We need to find out minimum steps a Knight will take to reach the target position.

Solution: This is basically find shortest path in unweighted graph. So we can use BFS
1) We try all 8 possible positions where a Knight can reach from its position.
If reachable position is not already visited and is inside the board, we push this state into queue with
distance 1 more than its parent state

In worst case, below code visits all cells of board, making worst-case time complexity as O(N^2)


***** Similar to shortest_distance_to_buildings.py *****
"""
from collections import deque


def min_step_to_reach_target(n, knight, target):
    if not n:
        return -1

    # 8 positions the knight can travel
    # '-' indicates up and left direction
    # '+' indicates down and right direction
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]

    q = deque()
    q.append((knight, 0))  # push starting position of knight with 0 distance

    visited = [[False] * n for _ in range(n)]

    # mark start state as visited
    visited[knight[0]][knight[1]] = True

    while q:
        position, dist = q.popleft()

        # current cell = target
        if position[0] == target[0] and position[1] == target[1]:
            return dist

        for i in range(8):
            tx = position[0] + dx[i]
            ty = position[1] + dy[i]

            # check if tx and ty are valid board positions
            if 0 <= tx < n and 0 <= ty < n and not visited[tx][ty]:
                visited[tx][ty] = True
                q.append(([tx, ty], dist + 1))

    # not reachable
    return -1

if __name__ == '__main__':
    n = 6
    knight = [3, 4]
    target = [0, 0]
    print min_step_to_reach_target(n, knight, target)

    target = [0, 1]
    print min_step_to_reach_target(n, knight, target)

    target = [3, 3]
    print min_step_to_reach_target(n, knight, target)
