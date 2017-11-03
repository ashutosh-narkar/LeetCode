#!/usr/bin/env python
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
def generate(self, numRows):
    if not numRows:
        return []

    result = []

    for i in range(numRows):
        result.append([1] * (i + 1))

        if i > 1:
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result



'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''
def getRow(rowIndex):

    if rowIndex < 0:
        return []

    prev_row = [1]

    for i in range(rowIndex):
        row = [1] # first element
 
        for j in range(1, i + 1):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1) # last element

        prev_row = row


    return prev_row
