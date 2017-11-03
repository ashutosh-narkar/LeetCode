#!/usr/bin/env python
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Solution:
We notice that the number of ways for the current step is the sum of the previous 2 steps

Say n = 5

n       number of ways
0       0
1       1
2       11, 2                (2 ways)
3       111,21,12            (3 ways)
4       1111,22,211,112,121  (5 ways)

'''
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    prev, current = 0, 1
    for i in range(n):
        prev, current = current, prev + current 
    return current





###### Using Recursion
# Time:  O(2^n)
# Space: O(n)
        
def climbStairs1(n):
                    
    if n == 1:
        return 1
                                        
    if n == 2:
        return 2
                                                            
    return climbStairs(n - 1) + climbStairs(n - 2)



########### Dynamic Programming
def climbStairs(n):

    # ith index represents the number of stairs. dp[i] is number of ways
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1 # number of ways to climb 0 or 1 step is 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

