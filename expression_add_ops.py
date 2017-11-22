#!/usr/bin/env python
"""
***** NOT YET PASSING ALL TESTS *****

Given a string that contains only digits 0-9 and a target value, return ALL possibilities to add binary operators
(not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []


Solution: Backtracking

**** Why this ?
For example, if you have a sequence of 12345 and you have proceeded to 1 + 2 + 3, now your eval is 6 right?
If you want to add a * between 3 and 4, you would take 3 as the digit to be multiplied,
so you want to take it out from the existing eval. You have 1 + 2 + 3 * 4 and the eval now is (1 + 2 + 3) - 3 + (3 * 4)
"""


def add_operators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """

    if not num:
        return []

    result = []
    backtrack(result, "", num, target, 0, 0, 0)
    return result


def backtrack(result, temp, num, target, start, current_eval, prev_eval):
    if start == len(num):
        if current_eval == target:
            result.append(temp)
            return

    for i in range(start, len(num)):

        # 0 sequence: because we can't have numbers with multiple digits started with zero
        if i != start and num[start] == '0':
            break

        cur_num = int(num[start: i + 1])

        # First number
        if start == 0:
            backtrack(result, temp + num[i], num, target, i + 1, cur_num, cur_num)

        else:
            backtrack(result, temp + '+' + num[i], num, target, i + 1, current_eval + cur_num, cur_num)

            backtrack(result, temp + '-' + num[i], num, target, i + 1, current_eval - cur_num, -cur_num)

            backtrack(result, temp + '*' + num[i], num, target, i + 1, current_eval - prev_eval + prev_eval * cur_num,
                      prev_eval * cur_num)    # Why this ? ****
