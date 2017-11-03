#!/usr/bin/env python
'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. 
The number of elements initialized in A and B are m and n respectively.
'''

# @param A  a list of integers
# @param m  an integer, length of A
# @param B  a list of integers
# @param n  an integer, length of B
# @return nothing(void)

def merge(A, m, B, n):

   i = m - 1
   j = n - 1
   k = m + n - 1


   # create an array of length m + n
   for z in range(n):
       A.append(0)

   while (i >= 0 and j >= 0):
       if A[i] >= B[j]:
           A[k] = A[i]
           k -= 1
           i -= 1

       else:
           A[k] = B[j]
           k -= 1
           j -= 1


   while j >= 0:
       A[k] = B[j]
       j -= 1
       k -= 1

   print A


if __name__ == '__main__':
    #merge([1,2,3], 3, [2, 5, 6], 3) 
    merge([], 0, [1], 1) 
       
