#!/usr/bin/env python
'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

def candy(ratings):

    if not ratings:
        return 0

    candy = [1] * len(ratings)

    # First, make sure I have right number of candy when compared to my left kid. 
    # Then, make sure I have the right number of candy when compared to my right kid.

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

            

    for i in range(len(ratings) -2, -1, -1):
        if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
            candy[i] = candy[i + 1] + 1

    return sum(candy)

