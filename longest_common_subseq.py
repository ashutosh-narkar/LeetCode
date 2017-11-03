#!/usr/bin/env python
'''
Given two strings 'X' and 'Y', find the length of the longest common subsequence. 
For example, if the given strings are 'aggtab' and 'gxtxayb', 
the output should be 4 as longest common substring is 'gtab'

Runtime = O(mn) where m = len(X) n = len(Y)
'''

import sys

def longest_common_subsequence_length(seq_x, seq_y):
    '''
    Take as input two sequences seq_x and seq_y
    Return length of longest common subsequence
    '''

    m = len(seq_x)
    n = len(seq_y)
   
    result = 0
 
    # initialize matrix to all neg values as we are taking max later
    alignment_matrix = [[float('-inf')] * (n + 1) for i in range(m + 1)] 


    for i in range(m + 1):
        for j in range(n + 1):

            # if either of the string is empty, 1st row and 1st col are 0
            if i == 0 or j == 0:
                alignment_matrix[i][j] = 0

            # consider rightmost characters of seq_x and seq_y
            elif seq_x[i - 1] == seq_y[j - 1]:
                alignment_matrix[i][j] = alignment_matrix[i - 1][j - 1] + 1

            # x matches with gap OR y matches with gap
            else:
                alignment_matrix[i][j] = max(alignment_matrix[i - 1][j], alignment_matrix[i][j - 1])

    return alignment_matrix[-1][-1], alignment_matrix


def get_longest_common_subsequence(length, matrix, x, y):

    nrows = len(matrix)
    ncols = len(matrix[0])


    # locate the start row and start col
    for i in range(nrows - 1, -1, -1):
        if length in matrix[i]:
            row = i
            col = matrix[i].index(length)
            break


    align_x, align_y = '', ''

    while row >= 0 and col >= 0:
        if matrix[row][col] == 0:
            break

        # case1: x and y matched
        val1 = matrix[row - 1][col - 1] + 1

        # case2: x matches with gap
        val2 = matrix[row - 1][col]

        # case3: y matches with gap
        val3 = matrix[row][col - 1]


        if matrix[row][col] == val1:
            align_x += x[row - 1]
            align_y += y[col - 1]
            row -= 1
            col -= 1

        elif matrix[row][col] == val2:
            align_x += x[row - 1]
            align_y += '-'
            row -= 1


        elif matrix[row][col] == val3:
            align_x += '-'
            align_y += y[col - 1]
            col -= 1
        

    return (align_x[::-1], align_y[::-1])




def main():
    x = sys.argv[1]
    y = sys.argv[2]

    len, matrix =  longest_common_subsequence_length(x, y)
    res =  get_longest_common_subsequence(len, matrix, x, y)

    print 'Longest commmon subseq between {} and {} is {} of length {}'.format(x, y, res, len)



if __name__ == '__main__':
    main()
