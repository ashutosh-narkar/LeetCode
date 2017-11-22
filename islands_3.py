#!/usr/bin/env python
"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which
turns the water at position (row, col) into a land.

Given a list of positions to operate, count the number of islands after each addLand operation.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

You may assume all four edges of the grid are all surrounded by water.

Solution: This is a basic union-find problem. Given a graph with points being added, we can at least solve:

How many islands in total?
Which island is pointA belonging to?
Are pointA and pointB connected?


The idea is simple. To represent a list of islands, we use trees. i.e., a list of roots.
This helps us find the identifier of an island faster. If roots[c] = p means the parent of node c is p,
we can climb up the parent chain to find out the identifier of an island.

To transform the two dimension problem into the classic UF, perform a linear mapping:

int id = n * x + y;

UNION operation is only changing the root parent so the running time is O(1).

FIND operation is proportional to the depth of the tree. If N is the number of points added,
the average running time is O(logN), and a sequence of 4N operations take O(NlogN).
If there is no balancing, the worse case could be O(N^2).
"""


def number_of_islands(m, n, positions):
    if m < 0 or n < 0:
        return 0

    nums = [-1] * (m * n)
    count = 0                  # number of islands

    result = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for pos in positions:
        root = n * pos[0] + pos[1]             # assume new point is isolated island
        nums[root] = root                      # add new island
        count += 1

        for i in range(4):
            x_coord = pos[0] + dx[i]
            y_coord = pos[1] + dy[i]

            nb = n * x_coord + y_coord

            if x_coord < 0 or x_coord >= m or y_coord < 0 or y_coord >= n or nums[nb] == -1:
                continue

            y = find(nums, nb)

            if y != root:                   # if neighbor is in another island
                nums[root] = y              # union two islands
                count -= 1

        result.append(count)

    return result


def find(nums, i):

    while nums[i] != i:
        nums[i] = nums[nums[i]]     # path compression
        i = nums[i]
    return i

if __name__ == '__main__':
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]

    print number_of_islands(m, n, positions)
