#!/usr/bin/env python
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.


Alternate Question:
Let A be an array of n numbers encoding the heights of adjacent
buildings of unit width. Design an algorithm to compute the area of the largest rectangle contained in this skyline

'''

def largestRectangleArea(height):

    if not height:
        return 0

        
    # Create an empty stack. The stack holds indexes of hist[] array
    # The bars stored in stack are always in INCREASING order of their
    # heights.
    stack= []

    max_area = 0  
    i = 0

    while (i < len(height)):

        # If this bar is higher than the bar on top stack, push it to stack
        if not stack or height[i] >= height[stack[-1]]:
            stack.append(i)
            i += 1
            
        # If this bar is lower than top of stack, then calculate area of rectangle 
        # height of rectangle =  stack top as the smallest (or minimum height) bar.
        # width of rectangle = 'i' is 'right index' for the top and element before top in stack is 'left index'
        else:

            top = stack.pop()   # height of rectangle
            width = i if not stack else i - 1 - stack[-1] # width of rectangle

            # update max area
            max_area = max(max_area, height[top] * width)

            
    # Now pop the remaining bars from stack and calculate area with every
    # popped bar as the smallest bar

    # if I have increasing heights as input eg (1,5,7), the first while loop will not give answer, in this case 
    # height of rectangle  = smallest  element of input
    # width of rectangle = 1
 
    while(stack):
        top = stack.pop()
        width = i if not stack else i - 1 - stack[-1]
        max_area = max(max_area, height[top] * width)
            

    return max_area



############################################################################
# Similar as above. We do not need the 2nd while loop if len(height) = 1 OR all heights are in increasing order
def largestRectangleArea(height):
    if not height:
        return 0


    # push a sentinel node back into the end of height to make the code logic more concise.
    # This handles cases where len(height)=1 OR height is in increasing order
    height.append(0)

    stack= []
    max_area = 0  

    for i in range(len(height)):
        if not stack or height[i] >= height[stack[-1]]:
            stack.append(i)

        else:
            # keep removing the top of stack while top of the stack is greater or till stack becomes empty
            # The building popped out represents the height of a rectangle with the new building as the right boundary
            # and the current stack top as the left boundary
            while (stack and height[stack[-1]] > height[i]):
                top = stack.pop()
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, height[top] * width)

            stack.append(i)

    return max_area












