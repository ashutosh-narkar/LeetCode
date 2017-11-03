#!/usr/bin/env python
'''
Given two sorted arrays A, B of size m and n respectively.
Find the k-th smallest element in the union of A and B.
You can assume that there are NO DUPLICATE elements.

Using two pointers, you can traverse both arrays without actually merging them, thus without the extra space. 
Both pointers are initialized to point to head of A and B respectively,
and the pointer that has the smaller of the two is incremented one step.
The k-th smallest is obtained by traversing a total of k steps.

Runtime - O(k)
'''

def findKthSmallest(num1, num2, k):

    if len(num1) + len(num2) < k:
        return -1

    m, n = 0, 0

    while True:

        # check if we fall off one list and if not, compare which list has smaller element
        if n == len(num2) or m < len(num1) and num1[m] < num2[n]:
            m += 1
            if m + n == k:
                return num1[m - 1]  # zero-based indexing 

        elif m == len(num1) or n < len(num2) and num2[n] < num1[m]:
            n += 1
            if m + n == k:
                return num2[n - 1]  # zero-based indexing

 


if __name__ == '__main__':
    a = [1,4,5,6,7,8,9,14,20]
    b = [2,3,10,12,13,16]
    #a = [1,2,3]
    #b = [4,5]

    for i in  range(1,(len(a) + len(b) + 1)):
        res = findKthSmallest(a, b, i)
        print '{}th smallest is {}'.format(i, res)


    # smallest number in the union
    res = findKthSmallest(a, b, 1)
    print 'Smallest number or 1st order statistic in the union is {}'.format(res)  
 

    # largest number in the union
    res = findKthSmallest(a, b, len(a) + len(b))
    print 'Largest number in the union {}'.format(res)  


    # Median in the union
    total_len = len(a) + len(b)
    med = (total_len + 1) / 2 if total_len % 2 else total_len / 2
    
    res = findKthSmallest(a, b, med)
    print 'Median of the union {}'.format(res)



  
