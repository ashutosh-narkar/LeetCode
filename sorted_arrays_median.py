#!/usr/bin/env python
'''
Median of Two Sorted Arrays 

There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Time Complexity: O(log n + log m)
Algorithmic Paradigm: Divide and Conquer


http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
'''

def findMedianSortedArrays(A, B):
    '''
    This method assumes that len(A) <= len(B) 
    '''

   
    # Smaller array has 1 element
    if len(A) == 1:

        # larger array has 1 element
        if len(B) == 1:
            return (A[0] + B[0]) / 2.0

        # larger array has odd length
        elif len(B) % 2 == 1:
            middle_index = (len(B) - 1) / 2
            middle = B[middle_index]

            val = getMedian([B[middle_index -1], B[middle_index + 1], A[0]])
            return (val + middle) / 2.0


        # larger array has even length
        else:
            middle_index = len(B) / 2
            mid1 = B[middle_index]
            mid2 = B[middle_index - 1]

            return getMedian([mid1, mid2, A[0]]) 
            


    # Smaller array has 2 elements
    elif len(A) == 2:

        # larger array has 2 elements
        if len(B) == 2:
            return getMedian([A[0], A[1], B[0], B[1]])

        # larger array has odd length
        elif len(B) % 2 == 1:
            middle_index = (len(B) - 1) / 2
            middle = B[middle_index]

            return getMedian([middle, max(B[middle_index - 1], A[0]), min(B[middle_index + 1], A[1])])
        
        # larger array has even length        
        else:
            middle_index = len(B) / 2
            mid1 = B[middle_index]
            mid2 = B[middle_index - 1]

            return getMedian([mid1, mid2, max(B[middle_index - 2], A[0]), min(B[middle_index + 1], A[1])])


    midA = len(A) / 2
    midB = len(B) / 2

    if A[midA] == B[midB]:
        return A[midA]

    if A[midA] > B[midB]:
        idx = len(A[midA + 1:]) # length of ignored part
        return findMedianSortedArrays(A[:midA + 1], B[idx:])

    else:
        idx = len(A[:midA]) # length of ignored part 
        return findMedianSortedArrays(A[midA:], B[:len(B) - idx + 1])


def getMedian(a):
    '''
    Return the median of the given numbers
    '''
    
    if len(a) == 3:
        return sum(a) - max(a) - min(a)

    if len(a) == 4:
        return (sum(a) - max(a) - min(a)) / 2.0


def findMedian(a, b):

    if a and not b:

        if len(a) % 2 == 1:
            middle = len(a) / 2
            return a[middle]    

        else:
            middle = len(a) / 2
            total = a[middle] + a[middle - 1]
            return total / 2.0

    if b and not a:
  
        if len(b) % 2 == 1:
            middle = len(b) / 2
            return b[middle]    
        else:
            middle = len(b) / 2
            total = b[middle] + b[middle - 1]
            return total / 2.0

    if len(a) <= len(b):
        return findMedianSortedArrays(a, b)

    else:
        return findMedianSortedArrays(b, a)

if __name__ == '__main__':

    a = [900]
    b = [5, 8, 10, 20]

    res = findMedian(a, b)
    assert res == 10


    a = [1, 12, 15, 26, 38]
    b = [2, 13, 17, 30, 45]

    a = []
    b = [1]
    res = findMedian(a, b)


    a = [1,2]
    b = [3,4,5,6]
    res = findMedian(a, b)
   
    a = []
    b = [1, 2, 3, 4, 5]
    res = findMedian(a, b)
    print res










 
