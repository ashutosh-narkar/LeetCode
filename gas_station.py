#!/usr/bin/env python
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.


Solution:
Every time arrive to the station, fill the max gas here, and consume the cost to go to the next

So by the time we cover all station(ie. complete for loop), if we have gas left we can complete the circuit
'''


# @param gas, a list of integers
# @param cost, a list of integers
# @return an integer

def canCompleteCircuit(gas, cost):

    loc = 0
    gas_left = 0
    min = float('inf')

    # find the minimum 
    for i in range(len(gas)):

        gas_left += gas[i] - cost[i]

        if gas_left < min:
            min = gas_left
            loc = i


    # cannot have negative tank
    if gas_left < 0:
        return -1

    # the station after loc is the starting station
    else:
        return (loc + 1) % len(gas)


if __name__ == '__main__':
    print canCompleteCircuit([1,2], [2,1])
