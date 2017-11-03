#!/usr/bin/env python
'''
Given k sorted arrays of size n each, merge them and print the sorted output.

Example:

Input:
k = 3, n =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Output: 0 1 2 3 4 5 6 7 8 9 10 11 


Solution:
We can merge arrays in O(nk*Logk) time using Min Heap. 

1. Create an output array of size n*k.
2. Create a min heap of size k and insert 1st element in all the arrays into a the heap
3. Repeat following steps n*k times.
     a) Get minimum element from heap and store it in output array.
     b) Replace heap root with next element from the array from which the element is extracted. If the array doesn't have any more elements, 
        then replace root with infinite. After replacing the root, heapify the tree.


Alternate question: Given an n x n matrix, where every row and column is sorted in non-decreasing order.
Print all elements of matrix in sorted order.


'''
from heapq import heappush, heappop

def mergekArrays(seq):

    k = len(seq)  # number of arrays
    n = len(seq[0])  # length of each array

    heap = []
    result = []

    for i in range(len(seq)):
        heappush(heap, (seq[i][0], i, 0))    # (element, row, col)

    for i in range(n * k):
        element, row, col = heappop(heap)

        result.append(element)

        # next element from the same row
        if col + 1 < n:
            val = seq[row][col + 1]
            heappush(heap, (val, row, col + 1))

        else:
            heappush(heap, (float('inf'), None, None))   # replace element by 'inf' as min element needed

    return result

if __name__ == '__main__':

    input = [[1, 3, 5],
            [2, 4, 6, 8],
            [0, 8, 9, 10]]

        
    print mergekArrays(input)


    input = [[10, 20, 30, 40],
             [15, 25, 35, 45],
             [27, 29, 37, 48],
             [32, 33, 39, 50]]
    
    print mergekArrays(input)

 
