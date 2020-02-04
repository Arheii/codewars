# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:26:54 2020

@author: Arh
"""
"""        0 1 2 3 4 5 6 7 8 """
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1], # <- 4,7
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

puzzle_hard = [[0, 0, 6, 1, 0, 0, 0, 0, 8], 
              [0, 8, 0, 0, 9, 0, 0, 3, 0], 
              [2, 0, 0, 0, 0, 5, 4, 0, 0], 
              [4, 0, 0, 0, 0, 1, 8, 0, 0], 
              [0, 3, 0, 0, 7, 0, 0, 4, 0], 
              [0, 0, 7, 9, 0, 0, 0, 0, 3], 
              [0, 0, 8, 4, 0, 0, 0, 0, 6], 
              [0, 2, 0, 0, 5, 0, 0, 8, 0], 
              [1, 0, 0, 0, 0, 2, 5, 0, 0]]

solution_hard = [[3, 4, 6, 1, 2, 7, 9, 5, 8], 
                [7, 8, 5, 6, 9, 4, 1, 3, 2], 
                [2, 1, 9, 3, 8, 5, 4, 6, 7], 
                [4, 6, 2, 5, 3, 1, 8, 7, 9], 
                [9, 3, 1, 2, 7, 8, 6, 4, 5], 
                [8, 5, 7, 9, 4, 6, 2, 1, 3], 
                [5, 9, 8, 4, 1, 3, 7, 2, 6],
                [6, 2, 4, 7, 5, 9, 3, 8, 1],
                [1, 7, 3, 8, 6, 2, 5, 9, 4]]

puzzle_inc1 =   [[2, 7, 0, 6, 0, 8, 0, 4, 0],
                [0, 0, 8, 0, 0, 0, 2, 0, 0],
                [0, 9, 0, 0, 0, 0, 3, 0, 0],
                [0, 5, 0, 0, 8, 2, 0, 0, 0],
                [0, 0, 0, 5, 0, 6, 0, 0, 0],
                [0, 0, 0, 9, 1, 0, 0, 5, 0],
                [0, 0, 7, 0, 0, 0, 0, 8, 0],
                [0, 0, 2, 0, 0, 0, 9, 0, 0],
                [0, 6, 0, 2, 0, 3, 0, 7, 4]]

puzzle_inc2 =  [[4, 7, 0, 3, 0, 2, 0, 6, 0],
                [0, 0, 9, 0, 0, 0, 2, 0, 0],
                [0, 8, 0, 0, 0, 0, 7, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 9, 0],
                [0, 0, 2, 0, 0, 0, 8, 0, 0],
                [0, 4, 0, 8, 0, 6, 0, 7, 2],
                [0, 5, 0, 0, 1, 9, 0, 0, 0],
                [0, 0, 0, 6, 0, 5, 0, 0, 0],
                [0, 0, 0, 2, 8, 0, 0, 5, 0]]

puzzle_inc3 =  [[5, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 4, 0, 2, 0, 8, 0, 6, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 5],
                [9, 0, 6, 0, 7, 0, 4, 0, 3],
                [0, 0, 0, 4, 0, 0, 2, 0, 0],
                [0, 7, 0, 0, 2, 3, 0, 1, 0],
                [0, 3, 0, 7, 0, 0, 0, 5, 0],
                [0, 0, 7, 0, 0, 5, 0, 0, 0],
                [4, 0, 5, 0, 1, 0, 7, 0, 8]]

puzzle_inc4 =  [[2, 7, 0, 6, 0, 8, 0, 4, 0],
                [0, 0, 8, 0, 0, 0, 2, 0, 0],
                [0, 9, 0, 0, 0, 0, 3, 0, 0],
                [0, 5, 0, 0, 8, 2, 0, 0, 0],
                [0, 0, 0, 5, 0, 6, 0, 0, 0],
                [0, 0, 0, 9, 1, 0, 0, 5, 0],
                [0, 0, 7, 0, 0, 0, 0, 8, 0],
                [0, 0, 2, 0, 0, 0, 9, 0, 0],
                [0, 6, 0, 2, 0, 3, 0, 7, 4],]

puzzle_inc5 =  [[0, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 0, 9, 0, 1, 5, 0, 2, 0],
                [0, 0, 7, 2, 0, 0, 0, 6, 0],
                [9, 0, 4, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 3, 0, 9, 0, 0, 0],
                [0, 0, 6, 0, 0, 0, 9, 0, 8],
                [0, 6, 0, 0, 0, 8, 5, 0, 0],
                [0, 1, 0, 9, 4, 0, 8, 0, 0],
                [0, 0, 0, 0, 0, 7, 0, 0, 0]]

test =  [[4, 7, 0, 3, 5, 2, 9, 6, 8],
         [5, 3, 9, 7, 6, 8, 2, 4, 1],
         [2, 8, 6, 9, 4, 1, 7, 3, 5],
         [8, 6, 3, 1, 2, 7, 5, 9, 4],
         [7, 9, 2, 5, 3, 4, 8, 1, 6],
         [1, 4, 5, 8, 9, 6, 3, 7, 2],
         [3, 5, 8, 4, 1, 9, 6, 2, 7],
         [9, 2, 4, 6, 7, 5, 1, 8, 3],
         [6, 1, 7, 2, 8, 3, 4, 5, 9]]

multi_answer = [[0, 0, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 0, 0, 3],
                [7, 8, 9, 0, 0, 3, 4, 5, 6],
                [0, 3, 4, 5, 6, 7, 8, 9, 0],
                [5, 6, 7, 8, 9, 0, 0, 3, 4],
                [8, 9, 0, 0, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 0, 0],
                [6, 7, 8, 9, 0, 0, 3, 4, 5],
                [9, 0, 0, 3, 4, 5, 6, 7, 8]]

import numpy as np
from itertools import product
from copy import deepcopy

def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    pzl = np.array(puzzle)
    if not is_sudoku(pzl):
        raise ValueError('Incorrect field')
    # Initialization
    zeros = {key:set(range(1,10)) for key in product(range(9), range(9)) if pzl[key]==0}
    friends = {key:nearest(pzl, *key) for key in product(range(9), range(9))}
    for key in product(range(9), range(9)):
        if pzl[key]:
            del_x_and_key_from_dicts(zeros, friends, pzl[key], key, start=True)     
    deep = 0
    solved_pzl = False
    snapshots = []
    
    while True:
        changes = False
        for key in set(zeros.keys()):
            if len(zeros[key]) > 1 and deep:
                zeros[key] = check_friends(zeros, friends, key)
            if len(zeros[key]) == 1:
                changes = True
                pzl[key] = zeros.pop(key).pop()
                del_x_and_key_from_dicts(zeros, friends, pzl[key], key)
            elif not zeros[key]: # founded collision
                if len(snapshots) > 0: # back to the last state
                    pzl, zeros, friends = snapshots.pop()
                elif solved_pzl: # only one solution
                    return solved_pzl

        if not changes:
            if deep > 1:
                temp  = zeros[key].pop()
                snapshots.append((pzl.copy(), deepcopy(zeros), deepcopy(friends)))
                zeros[key] = set([temp])
            else:
                deep += 1
        else:
            deep = 0
            
        if not zeros:
            if solved_pzl: # founded second solution
                raise ValueError('founded more then 1 solution')
            if snapshots and len(snapshots[-1][1]) < 100: # looking for other solutions
                solved_pzl = pzl.tolist()
                pzl, zeros, friends = snapshots.pop()
            else:
                return pzl.tolist()


def is_sudoku(pzl):
    """ Return True if we have correctly Sudoku field """
    if pzl.dtype == '<U1' or pzl.shape != (9,9):
        return False
    if np.any(pzl < 0) or np.any(pzl > 9):
        return False
    if np.sum(pzl != 0) < 17:
        return False
    for x in range(1,10):
        for i in range(9):
            c1 = np.sum(pzl[i,:] == x) > 1
            c2 = np.sum(pzl[i,:] == x) > 1
            square = pzl[i//3*3:(i//3+1)*3, i%3*3:(i%3+1)*3]
            c3 = np.sum(square == x) > 1
            if c1 or c2 or c3:
                return False
    return True

            
def nearest(pzl, n, m):
    """ returns coords of '0'.neighbors in a line, column, cell 3x3 """
    dk = ((0,1,2),(3,4,5),(6,7,8))
    row = set((n,j) for j in range(9) if pzl[n,j]==0 and (n, j) != (n, m))
    col = set((i,m) for i in range(9) if pzl[i,m]==0 and (i, m) != (n, m))
    squared = set((i,j) for i in dk[n//3] for j in dk[m//3] if pzl[i,j]==0 and (i, j)!=(n, m))
    return (row, col, squared)


def del_x_and_key_from_dicts(zeros, friends, x, key, start=False):
    """ deletes a value x in its row, column and 3cell
    also delete possible keys for friends """
    row, col, squared = friends.pop(key)
    for k in row | col | squared:
        zeros[k].discard(x)
        if not start:
            friends[k][0].discard(key)
            friends[k][1].discard(key)
            friends[k][2].discard(key)

    
def check_friends(zeros, friends, key):
    """ check if we have only one possible digit in block """
    row, col, squared = friends[key]
    digits = set(zeros[key])
    p1 = digits - set.union(*[zeros[k] for k in row])
    p2 = digits - set.union(*[zeros[k] for k in col])
    p3 = digits - set.union(*[zeros[k] for k in squared])
    found = p1 | p2 | p3
    if not found:
        return zeros[key]
    elif len(found) == 1: 
        return [found.pop()]    
    else:
        return []
    

from time import time
start = time()
for i in range (10):
    print('\npuzzle\n')
    answer = sudoku_solver(puzzle)
    print(np.array(answer))
    print(answer == solution)
    
    print('\npuzzle_hard\n')
    answer = sudoku_solver(puzzle_hard)
    print(np.array(answer))
    print(answer == solution_hard)
#    print("time first 2", time() - start)
    
    print('\ntest\n')
    answer = sudoku_solver(test)
    print(np.array(answer))
    
    print('\nincorrect1\n')
    answer = sudoku_solver(puzzle_inc1)
    print(np.array(answer))
    
    print('\nincorrect2\n')
    answer = sudoku_solver(puzzle_inc2)
    print(np.array(answer))
    
    print('\nincorrect4\n')
    answer = sudoku_solver(puzzle_inc4)
    print(np.array(answer))

end = time()
print('time ', end - start)
izm.append(end - start)
 
#print('\nincorrect4\n')
#answer = sudoku_solver(puzzle_hard)
#print(np.array(answer))
    