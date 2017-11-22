#!/usr/bin/env python
"""
Imagine you have a special keyboard with the following keys:
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                 after what has already been printed.

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the
output is M (No. of As that you can produce).

Examples:
Input:  N = 3
Output: 3
We can at most get 3 A's on screen by pressing
following key sequence.
A, A, A

Input:  N = 7
Output: 9
We can at most get 9 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Input:  N = 11
Output: 27
We can at most get 27 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A,
Ctrl C, Ctrl V, Ctrl V

Solution:

1) For N < 7, the output is N itself

2) For N > 6, the sequence of N keystrokes which produces an optimal string length will end with a suffix
of Ctrl-A, a Ctrl-C, followed by only Ctrl-V's

The task is to find out the breakpoint after which we get the above suffix of keystrokes.
Definition of a breakpoint is that instance after which we need to only press Ctrl-A, Ctrl-C once
and the only Ctrl-V's afterwards to generate the optimal length.

If we loop from N-3 to 1 and choose each of these values for the break-point,
and compute that optimal string they would produce. Once the loop ends, we will have the maximum of the
optimal lengths for various breakpoints, thereby giving us the optimal length for N keystrokes.

"""


# DP solution
def compute_max_dp(n):

    # The optimal string length is N when N is smaller than 7
    if n <= 6:
        return n

    # dp[i] indicates the number of A's for i keystrokes
    dp = [0] * (n + 1)

    # The optimal string length is N when N is smaller than 7
    for i in range(1, 7):
        dp[i] = i

    for i in range(7, n + 1):

        # For any keystroke n, we need to loop from n-3 keystrokes
        # back to 1 keystroke to find a breakpoint 'j' after which we
        # will have ctrl-a, ctrl-c and then only ctrl-v all the way.
        for j in range(i - 3, 0, -1):                                      # We range till index 1 and not 0
            temp = (i - j - 1) * dp[j]

            if temp > dp[i]:
                dp[i] = temp

    return dp[n]


# Recursive Solution
def compute_max_rec(n):

    # The optimal string length is N when N is smaller than 7
    if n < 7:
        return n

    # Initialize result
    result = 0

    # TRY ALL POSSIBLE BREAK-POINTS
    # For any keystroke N, we need to loop from N-3 keystrokes
    # back to 1 keystroke to find a breakpoint 'b' after which we
    # will have Ctrl-A, Ctrl-C and then only Ctrl-V all the way.
    for i in range(n - 3, 0, -1):
        # If the breakpoint is s at b'th keystroke then
        # the optimal string would have length
        # (n-b-1)*screen[b-1]
        temp = (n - i - 1) * compute_max_rec(i)

        if temp > result:
            result = temp

    return result

if __name__ == '__main__':
    assert compute_max_rec(3) == 3
    assert compute_max_rec(7) == 9
    assert compute_max_rec(11) == 27

    assert compute_max_dp(3) == 3
    assert compute_max_dp(7) == 9
    assert compute_max_dp(11) == 27

    print 'Tests Passed'
