#!/usr/bin/env python
'''
Arrange numbers such that all numbers at odd index are greater than that at even index
'''

def oddEvenSort(numbers):
    isSorted = False
    j = 0
    while(not isSorted):
        isSorted = True
        for i in range(0, len(numbers), 2):
            try:
                if numbers[i] > numbers[i + 1 + 2*j]:
                    numbers[i], numbers[i + 1 + 2*j] = numbers[i + 1 + 2*j], numbers[i]
                    isSorted = False
            except IndexError:
                break

        for i in range(1, len(numbers), 2):
            try:
                if numbers[i] < numbers[i + 1 + 2*j]:
                    numbers[i], numbers[i + 1 + 2*j] = numbers[i + 1 + 2*j], numbers[i]
                    isSorted = False
            except IndexError:
                break
        j += 1
        
    return numbers

if __name__ == '__main__':
    data = [12,6,10,5,23,1,33,3,44,4,55,5]
    print 'Original {}'.format(data)
    res = oddEvenSort(data)
    print 'Sorted {}'.format(res)     

    _max = float('-inf')
    for i in range(0, len(res), 2):
        _max = max(_max, res[i])


    _min = float('inf')
    for i in range(1, len(res), 2):
        _min = min(_min, res[i])
        

    print 'Largest number in even index {}'.format(_max)
    print 'Smallest number in odd index {}'.format(_min)     








 
