#!/usr/bin/env python
'''

LOOK AT SOLUTION 'search_matrix.py'

Searching a 2D Sorted Matrix. ie. rows and columns are sorted


'''
def find(numbers, val):
    row = 0
    col = len(numbers[0]) - 1

    if val < numbers[0][0] or val > numbers[len(numbers) - 1][col]:
        return -1

    while(row <= len(numbers) - 1 and col >= 0):
        if numbers[row][col] == val:
            return (row, col)

        elif val < numbers[row][col]:
            col -= 1

        else:
            row += 1


    return -1 # not found


if __name__ == '__main__':
     data = [[1,4,7,11,15],
             [2,5,8,12,19],
             [3,6,9,16,22],
             [10,13,14,17,24],
             [18,21,23,26,30],
             [32,34,45,60,80]]

     res = find(data, 30)
     assert res == (4, 4), 'wrong answer'

     res = find(data, 100)
     assert res == -1, 'wrong answer'

     print 'Tests passed !'


