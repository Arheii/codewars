# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:21:20 2020
returns the length of the easiest path through the mountains
kata 3
https://www.codewars.com/kata/576986639772456f6f00030c
@author: Arh
"""

a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

from heapq import heappop, heappush

def path_finder(area):
    area = [list(line) for line in area.split('\n')]
    N = len(area)

    steps = [(0, 0, 0)]
    while steps:
        print(steps)
        score, x, y = heappop(steps)
        if type(area[x][y]) == str:          
            if x == y == N - 1:
                print(*['   '.join([str(x) if type(x)==int else 'X' for x in line]) for line in area], sep='\n')
                return score
            alt = int(area[x][y])
            area[x][y] = score
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                i, j = x + dx, y + dy
                if -1 < i < N and -1 < j < N and type(area[i][j]) == str:                    
                    new_score = score + abs(int(area[i][j]) - alt)
                    heappush(steps, (new_score, i, j))
#            if y:   
#                heappush(steps, (score, x    , y - 1, alt))
#            if x:
#                heappush(steps, (score, x - 1, y    , alt))
#            if y < N:
#                heappush(steps, (score, x    , y + 1, alt))
#            if x < N:
#                heappush(steps, (score, x + 1, y    , alt))
    print(*['   '.join([str(x) if type(x)==int else 'X' for x in line]) for line in area], sep='\n')
    return False

#assert(path_finder(a)==0) 
assert(path_finder(b)==2)
#assert(path_finder(c)==4)
#assert(path_finder(d)==42)