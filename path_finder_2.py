# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:05:58 2020
Return the len the shortest path 
kata 4
https://www.codewars.com/kata/57658bfa28ed87ecfa00058a
@author: Arh
"""
from time import time
a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

e = "\n".join([
  ".WW...",
  ".W..W.",
  ".W.W..",
  ".W.W.W",
  ".W.W.W",
  "...W.."
])

f = "\n".join([
  "............",
  ".WWWW.W..W.W",
  ".W....W..W..",
  ".W.WW.W....W",
  ".W....W..W..",
  "...W..W..W..",
  "......W..W..",
  "...WWW..W..W",
  ".......W..WW",
  "...WWWWW....",
  "...W....WW.W",
  "...W........",
])

g =  ['.'*100 for _ in range(100)]
for i in range (1, 100, 2):
    g[i] = 'W' * (99 - i) + '..' + 'W' * (i-1)
g = "\n".join(g)
        
maze = f
M = 1000
 
cop = []
def path_finder(maze):
#    W = ['W']
#    N = maze.index('\n') - 1
#    maze = [W + list(line) + W for line in maze.split('\n')]
#    maze.append(W * (N + 2))
#    maze.insert(0, W * (N + 2))
    maze = [list(line) for line in maze.split('\n')]
    N = len(maze) - 1
    maze2 = [[10000] * (N+1) for _ in range(N+1)]
    shortest = False
    
    
    def find_rec(x, y, i, way):
        nonlocal shortest
        if maze2[x][y] <= i:
            return
        if x == y == N:
            shortest = i
            return
        if shortest and i + (N-x) + (N-y) >= shortest:
            return
        maze2[x][y] = i
        if way != 0 and x < N and maze[x+1][y] != 'W':
            find_rec(x + 1, y    , i + 1, 2)
        if way != 1 and y < N and maze[x][y+1] != 'W':
            find_rec(x    , y + 1, i + 1, 3)
        if way != 2 and x and maze[x-1][y] != 'W':
            find_rec(x - 1, y    , i + 1, 0)
        if way != 3 and y and maze[x][y-1] != 'W':
            find_rec(x    , y - 1, i + 1, 1)
        return
    
    find_rec(0, 0, 0, 2)
#    print(*['   '.join([str(x) if type(x)==int else x for x in line]) for line in maze], sep='\n')
    return shortest

 
start = time()
for _ in range(M):
    ans = path_finder(maze)
print('path_finder_rec', ans)
end = time()
print(f'Затрачено {end - start} секунд')


def path_finder_iter(maze):
#    N = maze.index('\n')
#    maze = [['W'] + list(line) + ['W'] for line in maze.split('\n')]
#    maze.append(['W'] * (N + 2))
#    maze.insert(0, ['W'] * (N + 2))
#    N = maze.index('\n') - 1
    maze = [list(line) for line in maze.split('\n')]
    N = len(maze) - 1
    maze2 = [[10000] * (N+1) for _ in range(N+1)]
    shortest = False
    
    steps = [[0, 0, 0]]
    while steps:
#        print(steps)
        x, y, i = steps.pop()
        if maze2[x][y] <= i:
            continue
        if x == y == N:
            shortest = i
            continue
        if shortest and i + 2 * N - x - y >= shortest:
            continue
        maze2[x][y] = i
        if y and maze[x][y-1] != 'W':
            steps.append([x    , y - 1, i + 1])
        if x and maze[x-1][y] != 'W':
            steps.append([x - 1, y    , i + 1])
        if y < N and maze[x][y+1] != 'W':
            steps.append([x    , y + 1, i + 1])
        if x < N and maze[x+1][y] != 'W':
            steps.append([x + 1, y    , i + 1])
    
#    print(*['   '.join([str(x) if type(x)==int else x for x in line]) for line in maze], sep='\n')
    return shortest

start = time()
for _ in range(M):
    ans = path_finder_iter(maze)
print('path_finder_iter', ans)
end = time()
print(f'Затрачено {end - start} секунд')


def path_finder_ref1(maze):
    maze = [list(line) for line in maze.split('\n')]
    N = len(maze) - 1

    steps = [[0, 0, 0]]
    while steps:
        x, y, i = steps.pop(0)
        if maze[x][y] == '.':
            if x == y == N:
                return i
            maze[x][y] = i
            if y:
                steps.append([x    , y - 1, i + 1])
            if x:
                steps.append([x - 1, y    , i + 1])
            if y < N:
                steps.append([x    , y + 1, i + 1])
            if x < N:
                steps.append([x + 1, y    , i + 1])
    return False


start = time()
for _ in range(M):
    ans = path_finder_ref1(maze)
print('path_finder_ref1', ans)
end = time()
print(f'Затрачено {end - start} секунд')

from heapq import heappop, heappush
def path_finder_heap(maze):
    maze = [list(line) for line in maze.split('\n')]
    N = len(maze) - 1

    steps = [(0, 0, 0)]
    while steps:
        i, x, y = heappop(steps)
        if maze[x][y] == '.':
            if x == y == N:
                return i
            maze[x][y] = i
            if y:
                heappush(steps, (i + 1, x    , y - 1))
            if x:
                heappush(steps, (i + 1, x - 1, y    ))
            if y < N:
                heappush(steps, (i + 1, x    , y + 1))
            if x < N:
                heappush(steps, (i + 1, x + 1, y    ))
    return False


start = time()
for _ in range(M):
    ans = path_finder_heap(maze)
print('path_finder_heap', ans)
end = time()
print(f'Затрачено {end - start} секунд')