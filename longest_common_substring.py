#!/usr/bin/env python
'''
Given two strings 'X' and 'Y', find the length of the longest common substring. 
For example, if the given strings are 'GeeksforGeeks' and 'GeeksQuiz', 
the output should be 5 as longest common substring is 'Geeks'

Runtime = O(mn) where m = len(X) n = len(Y)
'''

import sys

def longest_common_substring_length(seq_x, seq_y):
    '''
    Take as input two sequences seq_x and seq_y
    Return length of longest common substring
    '''

    m = len(seq_x)
    n = len(seq_y)
   
    result = 0
 
    # initialize matrix to all neg values as we are taking max later
    alignment_matrix = [[float('-inf')] * (n + 1) for i in range(m + 1)] 


    for i  in range(m + 1):
        for j in range(n + 1):

            # if either of the string is empty, 1st row and 1st col are 0
            if i == 0 or j == 0:
                alignment_matrix[i][j] = 0

            # consider rightmost characters of seq_x and seq_y
            elif seq_x[i - 1] == seq_y[j - 1]:
                alignment_matrix[i][j] = alignment_matrix[i - 1][j - 1] + 1
                result = max(result, alignment_matrix[i][j])

            else:
                alignment_matrix[i][j] = 0

    return result, alignment_matrix

def get_longest_common_substring(length, matrix, x):
    '''
    start from the position where the optimal length is 
    located in the alignment matrix.
    
    Move along the diagonal till matrix element is non-zero
    '''

    nrows = len(matrix)
    ncols = len(matrix[0])

    row, col = 0, 0

    # locate the start row and start col
    for i in range(nrows - 1, -1, -1):
        if length in matrix[i]:
            row = i
            col = matrix[i].index(length)
            break

 
    result = ''
    while row >= 0 and col >= 0:
        if matrix[row][col] == 0:
            break
        
        # save result
        result += x[row - 1]

        # move up along diagonal
        row -= 1
        col -= 1

    return result[::-1]
        

def main():
    x = sys.argv[1]
    y = sys.argv[2]

    len, matrix =  longest_common_substring_length(x, y)
    res = get_longest_common_substring(len, matrix, x)

    print 'Longest commmon substring between {} and {} is {} of length {}'.format(x, y, res, len)



if __name__ == '__main__':
    main()
