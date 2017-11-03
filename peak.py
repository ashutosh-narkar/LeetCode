#/usr/bin/env python
'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -inf

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Runtime = O(log n)
'''

def findPeakElement(num):

    if not num:
        return


    if len(num) == 1:
        return 0


    idx = [-1]
    find(num, 0, len(num) - 1, idx)
    return idx[0]

def find(num, low, high, idx):

    if low > high or idx[0] != -1:
        return

    else:
        mid = low + (high - low)/2



        # if mid is 1st index
        if mid == 0 and num[mid] > num[mid + 1]:
            idx[0] =  mid
            return

        # if mid is last index
        if mid == len(num) - 1 and num[mid] > num[mid - 1]:
            idx[0] =  mid
            return

        # if mid is not at edges
        if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
            idx[0] =  mid
            return


        find(num, low, mid - 1, idx)
        find(num, mid + 1, high, idx)

#################################################################################################
# Using normal Binary Search
# conditions num[i] != num[i + 1] and num[-1] and num[n] = -inf, guarantee accuracy of Binary Search 

def findPeakElement(self, num):

    if not num:
        return

    if len(num) == 1:
        return 0

    low = 0
    high = len(num) - 1

    # NO '<='
    while (low < high):
        mid = low + (high - low) / 2

        if num[mid] > num[mid + 1] and num[mid] > num[mid - 1]:
            return mid

        elif num[mid] > num[mid + 1]:
            high = mid - 1

        else:
            low = mid + 1

    if num[low] > num[high]:
        return low
    else:
        return high





if __name__ == '__main__':
    data = [1, 1, 1, 1, 4,5,0]

    print 'For {} index of peak is {}'.format(data, findPeakElement(data))
       
