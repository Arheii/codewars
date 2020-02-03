# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:26:54 2020

@author: Arh
"""

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
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

puzzle_inc =   [[2, 7, 0, 6, 0, 8, 0, 4, 0],
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

test =  [[4, 7, 0, 3, 5, 2, 9, 6, 8],
         [5, 3, 9, 7, 6, 8, 2, 4, 1],
         [2, 8, 6, 9, 4, 1, 7, 3, 5],
         [8, 6, 3, 1, 2, 7, 5, 9, 4],
         [7, 9, 2, 5, 3, 4, 8, 1, 6],
         [1, 4, 5, 8, 9, 6, 3, 7, 2],
         [3, 5, 8, 4, 1, 9, 6, 2, 7],
         [9, 2, 4, 6, 7, 5, 1, 8, 3],
         [6, 1, 7, 2, 8, 3, 4, 5, 9]]

import numpy as np


def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    pzl = np.array(puzzle)
    if not is_sudoku(pzl):
        return False

    zeros = {(i, j):range(1,10) for i in range(9) for j in range(9) if pzl[i,j]==0}
    dk = ((0,1,2),(3,4,5),(6,7,8))
    deep = 0
    solved_copy = False
    snapshots = []
    while True:
        check_dif = len(zeros)
        for key in set(zeros.keys()):
            zeros[key] = check_cell(pzl, zeros, *key, dk, deep=deep)
            if len(zeros[key]) == 1:
                pzl[key] = zeros.pop(key)[0]
            elif not zeros[key]: # была ошибка в предсказании
#                print("COLLISION FOUND, BACK TO STEP", len(snapshots) - 1)
                if snapshots:
                    print("otkat na", len(snapshots) - 1)
                    pzl, zeros = snapshots.pop()
                elif used_predictions: # Есть только одно решение
                    return pzl, zeros
        if check_dif == len(zeros): # Если нет найденных, увеличиваем глубину поиска
            if deep > 2: # Если ничего не помогает, начинаем предполагать
                temp, zeros[key] = zeros[key][0], zeros[key][1:]
                snapshots.append((pzl.copy(), zeros.copy()))
                zeros[key] = [temp]
                used_predictions = True
            else:
                deep += 1
        else:
            deep -= 1
            
        if not zeros:
            if solved_copy:
                return False
            elif snapshots:
                solved_copy = pzl.copy()
                pzl, zeros = snapshots.pop()
            else:
                return pzl, snapshots


def check_cell(pzl, zeros, n, m, dk, deep):
    """return digit for cell if found it, else 0"""
    digits = zeros[(n,m)]
    digits = [x for x in digits if x not in pzl[n,:]]
    digits = [x for x in digits if x not in pzl[:,m]]
    square = pzl[3 * (n // 3):3 * (n // 3) + 3, 3 * (m // 3): 3 * (m // 3) + 3]
    digits = [x for x in digits if x not in square.flat]
    if deep:
        pot = sum([zeros[(n,j)] for j in range(9) if pzl[n,j]==0], [])
#        print(potential, 'for', (n,m))
        found1 = list(filter(lambda x: list(pot).count(x)==1, digits))
        pot = sum([zeros[(i,m)] for i in range(9) if pzl[i,m]==0], [])
        found2 = list(filter(lambda x: list(pot).count(x)==1, digits))
        square = [(i,j) for i in dk[n//3] for j in dk[m//3]]
        pot = sum([zeros[(i,j)] for i,j in square if pzl[i,j]==0], [])
        found3 = list(filter(lambda x: pot.count(x)==1, digits))
        found = max(found1, found2, found3)
        if len(found) > 1: # for backward to previous version pzl
            return []
        elif len(found) == 1:
#            print('found', (n,m), found, 'square')
            return found
        
    return digits

def is_sudoku(pzl):
    """ Return True if we have correctly Sudoku field """
    if pzl.dtype != 'int32' or pzl.shape != (9,9):
        return False
    if np.all(pzl < 0) or np.all(pzl > 9):
        return False
    if np.sum(pzl != 0) < 17:
        return False
    for x in range(1,10):
        for i in range(9):
            c1 = np.sum(pzl[i,:] == x) > 2
            c2 = np.sum(pzl[i,:] == x) > 2
            square = pzl[i//3*3:(i//3+1)*3, i%3*3:(i%3+1)*3]
            c3 = np.sum(square == x) > 2
            if c1 or c2 or c3:
                return False
    return True



from time import time
start = time()
answer, zeros = sudoku_solver(puzzle)
print(np.array(answer))
print(answer == solution)

answer, zeros = sudoku_solver(puzzle_hard)
print(np.array(answer))
print(answer == solution_hard)

answer, snapshots = sudoku_solver(test)
print(np.array(answer))
print(answer == solution_hard)

answer, snapshots = sudoku_solver(puzzle_inc)
print(np.array(answer))
print(answer == solution_hard)

answer, snapshots = sudoku_solver(puzzle_inc2)
print(np.array(answer))
print(answer == solution_hard)


end = time()
print('time ', end - start)
izm.append(end - start)