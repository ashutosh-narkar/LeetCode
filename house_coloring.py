#!/usr/bin/env python
'''
There are a row of houses, each house can be painted with three colors red, blue and green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color. 
You have to paint the houses with minimum cost. How would you do it?


Note: Painting house-1 with red costs different from painting house-2 with red. The costs are different for each house and each color.


Approach:
Dynamic Programming solution:
we can paint the ith house with blue, red or green.
so we have the following equations:
cost[i,r] = min( cost[i-1,b], cost[i-1,g] ) + cost of painting i with r.
cost[i,g] = min( cost[i-1,b], cost[i-1,r] ) + cost of painting i with g.
cost[i,b] = min( cost[i-1,r], cost[i-1,g] ) + cost of painting i with b.


Final Min Cost = min (cost[n,b], cost[n,r], cost[n,g]);
'''

index_color = {0: 'RED', 1: 'GREEN', 2: 'BLUE'}

def houseColoring(colorMarix):
    nhouses = len(colorMarix) - 1

    # 2-D matrix with rows indicating the house number
    # cols indicate the colors R, G, B respectively
    # first row of matix is 0, since 0 houses
    house_cost  = [[0, 0, 0]]


    for i in range(1, nhouses + 1):
        row = []  
  
        # Case1: color ith house red
        cost_current_red = colorMarix[i][0]
        cost_prev_blue = house_cost[i - 1][2]
        cost_prev_green = house_cost[i - 1][1]

        # cost of painting i houses
        overall_cost = cost_current_red + min(cost_prev_blue, cost_prev_green)
        row.insert(0, overall_cost)



        # Case2: color ith house green
        cost_current_green = colorMarix[i][1]
        cost_prev_red = house_cost[i - 1][0]
        cost_prev_blue = house_cost[i - 1][2]

        # cost of painting i houses
        overall_cost = cost_current_green + min(cost_prev_blue, cost_prev_red)
        row.insert(1, overall_cost)


        # Case3: color ith house blue
        cost_current_blue = colorMarix[i][2]
        cost_prev_red = house_cost[i - 1][0]
        cost_prev_green = house_cost[i - 1][1]

        # cost of painting i houses
        overall_cost = cost_current_blue + min(cost_prev_red, cost_prev_green)
        row.insert(2, overall_cost)

        house_cost.insert(i, row)  



    overall_min = min(house_cost[-1])       
    return overall_min, house_cost


def colorsUsed(solution):
    '''
    Given the solution matrix find the
    colors used to paint each house
    '''
    nrows  = len(solution)
    row = nrows - 1

    while(row > 0):
        min_val = min(solution[row]) 
        index = solution[row].index(min_val)

        print 'House {} is painted {}'.format(row, index_color[index])

        row -= 1
        solution[row][index] = float('inf')

    
def main():

    # [R, G, B]
    colorMarix = [[0, 0, 0],
                  [7, 5, 10],
                  [3, 6, 1],
                  [8, 7, 4],
                  [6, 2, 9],
                  [1, 4, 7],
                  [2, 3, 6]]    


    min_cost, optimal_sol = houseColoring(colorMarix)
    print 'Min cost of house painting is {}'.format(min_cost)
    colorsUsed(optimal_sol)


if __name__ == '__main__':
    main()
         







