#!/usr/bin/env python
'''
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence 
such that all elements of the subsequence are sorted in increasing order. 

For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

'''
# Solution 1: Patience Sorting. O(nlogn)
'''
for each num in nums
     if(list.size()==0)
          add num to list
     else if(num > last element in list)
          add num to list
     else 
          replace the element in the list which is the smallest but bigger than num
'''


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    seq = []

    for num in nums:
        if not seq or num > seq[-1]:
            seq.append(num)

        else:
            low = 0
            high = len(seq) - 1

            while low < high:                          # NOT low <= high like traditional binary search
                mid = low + (high - low) / 2

                if seq[mid] < num:                     # If the element at mid is less than current, them move right as
                    low = mid + 1                      # all element to the left of mid will be smaller than current num

                else:                                  # if the number at mid is >= current number, DO NOT move high = mid - 1.
                    high = mid                         # If we do that, we will lose the number at index mid.

            seq[high] = num                            # OR seq[low] = num

    return len(seq)



# Solution 2: DP.  Runtime O(n^2)


def lis(seq):
    if not seq:
        return

    # Let arr[0..n-1] be the input array and dp(i) be the length of the LIS till index i such that arr[i] 
    # is part of LIS and arr[i] is the last element in LIS
    # hence initialize dp to 1
    dp = [1] * len(seq)
    max_len = 0
    

    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                
                # update max length
                max_len = max(max_len, dp[i])

    return max_len


if __name__ == '__main__':
    input = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print 'Length of longest increasing subsequence for {} is {}'.format(input, lis(input))
