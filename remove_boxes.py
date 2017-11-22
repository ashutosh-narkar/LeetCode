#!/usr/bin/env python
"""
***SOLUTION NOT YET GIVING THE RIGHT ANSWER***

Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
remove them and get k*k points.

Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Solution:

dp[i][j][k] means the max points from box[i] to box[j] with k boxes of value box[i] merged

We have two DP conditions

1) We choose to merge k boxes
this mean we would have score = dp(i+1, j, 1) + k * k ...............(1)

2) We don't merge k boxes
So, we can continue to find similar boxes
this means when we find box m equal to box i, we can have one more box, so k become k + 1
So we have dp(i+1, m-1, 1) + dp (m, j, k + 1) ...............(2)
the first term is the other boxes
and the second term contain information of the same boxes(box[i] or box[m]) we have found till now

dp[i][j][k] = max ((1), (2))
"""


def remove_boxes(boxes):
    """
    :type boxes: List[int]
    :rtype: int
    """
    if not boxes:
        return 0

    n = len(boxes)

    dp = [[[0] * n] * n for _ in range(n)]

    return helper(boxes, dp, 0, n - 1, 1)


def helper(boxes, dp, start, end, k):
    if start > end:
        return 0

    if start == end:
        return k * k

    if dp[start][end][k] != 0:
        return dp[start][end][k]

    score = helper(boxes, dp, start + 1, end, 1) + k * k

    for i in range(start + 1, end + 1):
        if boxes[start] == boxes[i]:
            score = max(score, helper(boxes, dp, start + 1, i - 1, 1) + helper(boxes, dp, i, end, k + 1))

    dp[start][end][k] = score
    return score
