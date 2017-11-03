#!/usr/bin/env python
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum
Runtime O(n)

Possible divide and conquer solution - https://leetcode.com/discuss/694/how-solve-maximum-subarray-using-divide-and-conquer-approach
'''

def maxSubArray(numbers):
    if not numbers:
        raise ValueError

    # if the list has all negative numbers, return 0 as max_sum
    # to return the largest negative number as max_sum
    # set max_sum = numbers[0]
    max_sum = numbers[0]
    current_sum = numbers[0]
    array = [] 
    for num in numbers[1:]:
        #array.append(num)
        if current_sum >= 0:
            current_sum += num
        else:
            current_sum = num
            array = [] 
        
        max_sum = max(max_sum, current_sum)
       # if max_sum < current_sum:
       #     max_sum = current_sum
       # else:
       #     array.remove(num)

    #idx1 = numbers.index(array[0])
    #idx2 = numbers.index(array[-1])
    #print 'Max subarray {}'.format(numbers[idx1:idx2+1])
    return max_sum

def maxSubArray_2(numbers):
    max_sum = numbers[0]
    current_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == '__main__':
    #data = [1,2,3,-5,-4,6,7,8,-10,45,6,7,8,-10]
    data  = [1, 2, -4, 1, 3, -2, 3, -1]
    _sum1 = maxSubArray_2(data)
    _sum2 = maxSubArray(data)
    print 'Using iterative_2: Max sum is {}'.format(_sum1)
    print 'Using iterative: Max sum is {}'.format(_sum2)
