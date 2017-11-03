#!/usr/bin/env python
'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
represent different tasks.Tasks could be done without original order.
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

Solution:
1) Get frequency of all tasks
2) Get the frequency count for the task to be performed the most
3) If you have 'n' identical tasks and need to separate by 'k' steps, it needs (k+1)*(n-1) + 1 steps.
4) If you have 'm' tasks all appear 'n' times, it would take (k+1)*(n-1) + m when m <= k
5) All other tasks should be able to fill in the empty steps.

If all empty steps are filled out (ie. didn't waste any spots (waste = being idle)), then we do not need empty steps,
the overall cost would be the size of input tasks. This means the number of slots in tasks array are already
large enough to accommodate this arrangement

Similar question: rearrange_str.py ***** TRY TO SOLVE WITH THAT ALGO****
'''


def least_interval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    if not tasks:
        return 0

    freqCount = [0] * 26  # one index for each alphabet
    maxFreq = 0

    for task in tasks:
        index = ord(task) - ord('A')
        freqCount[index] += 1

        if freqCount[index] > maxFreq:
            maxFreq = freqCount[index]

    # 'maxFreq' identical tasks and need to separated by 'n' steps
    ans = (maxFreq - 1) * (n + 1)


    for i in range(len(freqCount)):
        #  'maxFreq' tasks appears again
        if freqCount[i] == maxFreq:
            ans += 1

    return max(ans, len(tasks))