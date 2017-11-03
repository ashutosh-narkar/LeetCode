#!/usr/bin/env python
'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n^2.


Solution:
1) Main loop is binary search of max number in matrix  - min number in matrix
2) Swap from left-bottom to right-top and get count <= mid in O(n) time
3) Total complexity will be O(n logm) while m = max - min.

'''



def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        low = matrix[0][0]     # lowest number in matrix
        high = matrix[-1][-1]  # highest number in matrix

        while low <= high:
            mid = low + (high - low) / 2

            # find all numbers smaller than 'mid'
            count = getLessEqual(matrix, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid - 1

        return low


# start from the bottom-left corner and find the number of elements less than 'target'
def getLessEqual(matrix, target):
    nrows = len(matrix)
    ncols = len(matrix[0])

    i = nrows - 1
    j = 0

    result = 0
    while i >= 0 and j < ncols:
        num = matrix[i][j]

        if num > target:
            i -= 1

        else:
            result += i + 1    # 'i + 1' because all numbers till index 'i' are smaller than the target
            j += 1

    return result
