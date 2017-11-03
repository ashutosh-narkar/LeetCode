#!/usr/bin/env python

# Write a function that will return a list of integers that occur only once in a given array of integers.

def returnUnique(numbers):

    if not numbers:
        return 
        
    unique = {}
    for num in numbers:
        if num not in unique:
            unique[num] = 1
        else:
            unique[num] += 1
            
    result = []
    for val, count in unique.items():
        if count == 1:
            result.append(val)
            
    return result


if __name__ == '__main__':
    
    print returnUnique([1,2,2,2])
 
