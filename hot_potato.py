#!/usr/bin/env python

# Simulation: Hot Potato (http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html)


from collections import deque

def hotPotato(namelist, num):
    queue = deque(namelist)
    
    while len(queue) > 1:
        for i in range(num):
            player = queue.popleft()
            queue.append(player)
        queue.popleft()

    return queue.pop()


if __name__ == '__main__':
    print hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)
