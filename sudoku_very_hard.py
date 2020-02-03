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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======

>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
from itertools import product
from copy import deepcopy
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py

def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    pzl = np.array(puzzle)
    if not is_sudoku(pzl):
<<<<<<< HEAD
<<<<<<< HEAD
        raise IOError('Incorrect field')
=======
        return False
<<<<<<< HEAD
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py

    zeros = {(i, j):range(1,10) for i in range(9) for j in range(9) if pzl[i,j]==0}
    dk = ((0,1,2),(3,4,5),(6,7,8))
=======
        return False
    
    # Inicialisation
    ind_9x9 = product(range(9), range(9))
    zeros = {key:list(range(1,10)) for key in product(range(9), range(9)) if pzl[key]==0}
    friends = {key:nearest(pzl, *key) for key in product(range(9), range(9))}
#    return pzl, friends
    for key in ind_9x9:
        if pzl[key]:
            del_x_and_key_from_dicts(zeros, friends, pzl[key], key, start=True)
#    return pzl, zeros, friends
#    print(zeros, '\n\n', friends)
            
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
    deep = 0
    solved_pzl = False
    snapshots = []
    while True:
        check_dif = len(zeros)
#        print(check_dif)
        for key in set(zeros.keys()):
            if len(zeros[key]) > 1:
                zeros[key] = check_friends(zeros, friends, key)
            if len(zeros[key]) == 1:
#                print('найдено', key, zeros[key][0], zeros[key][0]==sol[key])
                pzl[key] = zeros.pop(key)[0]
                del_x_and_key_from_dicts(zeros, friends, pzl[key], key)
            elif not zeros[key]: # была ошибка в предсказании
#                print("COLLISION FOUND, BACK TO STEP", len(snapshots) - 1)
                if snapshots:
<<<<<<< HEAD
                    print("otkat na", len(snapshots) - 1)
                    pzl, zeros = snapshots.pop()
<<<<<<< HEAD
<<<<<<< HEAD
                elif solved_copy: # Есть только одно решение
                    return solved_copy
        if check_dif == len(zeros): # Если нет найденных, увеличиваем глубину поиска
            if deep > 1: # Если ничего не помогает, начинаем предполагать
                temp, zeros[key] = zeros[key][0], zeros[key][1:]
                snapshots.append((pzl.copy(), zeros.copy()))
                zeros[key] = [temp]
=======
                elif used_predictions: # Есть только одно решение
                    return pzl, zeros
        if check_dif == len(zeros): # Если нет найденных, увеличиваем глубину поиска
=======
                elif used_predictions: # Есть только одно решение
                    return pzl, zeros
        if check_dif == len(zeros): # Если нет найденных, увеличиваем глубину поиска
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
            if deep > 2: # Если ничего не помогает, начинаем предполагать
                temp, zeros[key] = zeros[key][0], zeros[key][1:]
                snapshots.append((pzl.copy(), zeros.copy()))
                zeros[key] = [temp]
                used_predictions = True
<<<<<<< HEAD
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
#                    print("otkat na", len(snapshots) - 1)
                    pzl, zeros, friends = snapshots.pop()
                elif solved_pzl: # Есть только одно решение
                    print('1st way')
                    return solved_pzl, zeros
                else:
#                    print("Переделывай")
                    return pzl, zeros
                
        print(len(zeros))
        if check_dif == len(zeros): # Если нет найденных, увеличиваем глубину поиска
            if deep > 3: # Если ничего не помогает, начинаем предполагать
                try:
#                    print('used timeline')
#                    print(key, zeros[key])
                    temp, zeros[key] = zeros[key][0], zeros[key][1:]
#                    pzl, zeros, friends = snapshots.pop()
                    snapshots.append((pzl.copy(), deepcopy(zeros), deepcopy(friends)))
                    zeros[key] = [temp]
#                    print(temp)
                    
                except:
#                    print('err timeline')
                    return pzl, zeros
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
            else:
                deep += 1
        else:
            deep -= 1
            
        if not zeros:
<<<<<<< HEAD
            if solved_copy:
<<<<<<< HEAD
<<<<<<< HEAD
                raise IOError('More then 1 solution')
            if snapshots:
                solved_copy = pzl.tolist()
                pzl, zeros = snapshots.pop()
            else:
                return pzl.tolist()
=======
                return False
            elif snapshots:
                solved_copy = pzl.copy()
                pzl, zeros = snapshots.pop()
            else:
                return pzl, snapshots
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
                return False
            elif snapshots:
                solved_copy = pzl.copy()
                pzl, zeros = snapshots.pop()
            else:
                return pzl, snapshots
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py


def check_cell(pzl, zeros, n, m, dk, deep):
    """return digit for cell if found it, else 0"""
    digits = zeros[(n,m)]
    digits = [x for x in digits if x not in pzl[n,:]]
    digits = [x for x in digits if x not in pzl[:,m]]
    square = pzl[3 * (n // 3):3 * (n // 3) + 3, 3 * (m // 3): 3 * (m // 3) + 3]
    digits = [x for x in digits if x not in square.flat]
    if deep:
        pot = sum([zeros[(n,j)] for j in range(9) if pzl[n,j]==0], [])
<<<<<<< HEAD
<<<<<<< HEAD
=======
#        print(potential, 'for', (n,m))
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
#        print(potential, 'for', (n,m))
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
        found1 = list(filter(lambda x: list(pot).count(x)==1, digits))
        pot = sum([zeros[(i,m)] for i in range(9) if pzl[i,m]==0], [])
        found2 = list(filter(lambda x: list(pot).count(x)==1, digits))
        square = [(i,j) for i in dk[n//3] for j in dk[m//3]]
        pot = sum([zeros[(i,j)] for i,j in square if pzl[i,j]==0], [])
        found3 = list(filter(lambda x: pot.count(x)==1, digits))
        found = max(found1, found2, found3)
<<<<<<< HEAD
<<<<<<< HEAD
        if len(found) > 1: # backward to previous snapshot pzl
            return []
        elif len(found) == 1:
            return found
        
    return digits

def is_sudoku(pzl):
    """ Return True if we have correctly Sudoku field """
    if pzl.dtype == '<U1' or pzl.shape != (9,9):
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
=======
            if solved_pzl: # нашлось второе решение
                raise IOError('found more then 1 solution')
                return False, zeros
            if snapshots: # ищем другие решения
                print('!Found 1 desition')
                solved_pzl = pzl.tolist()
                pzl, zeros, friends = snapshots.pop()
            else:
                return pzl.tolist(), snapshots
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py

            
def nearest(pzl, n, m):
    """ returns coords of '0'.neighbors in a line, column, cell 3x3 """
    dk = ((0,1,2),(3,4,5),(6,7,8))
    row = [(n,j) for j in range(9) if pzl[n,j]==0 and (n, j) != (n, m)]
    col = [(i,m) for i in range(9) if pzl[i,m]==0 and (i, m) != (n, m)]
    squared = [(i,j) for i in dk[n//3] for j in dk[m//3] if pzl[i,j]==0 and (i, j) != (n, m)]
    return (row, col, squared)


def del_x_and_key_from_dicts(zeros, friends, x, key, start=False):
    """ delete found x from line, col and squared.
    also delete possible keys from friends """
    row, col, squared = friends[key]
    for k in set(row+col+squared):
        if x in zeros[k]:
            zeros[k].remove(x)
        if not start:
            if k in row:
                friends[k][0].remove(key)
            if k in col:
                friends[k][1].remove(key)
            if k in squared:
                friends[k][2].remove(key)
    friends.pop(key)

    
def check_friends(zeros, friends, key):
#    print('ch_f for', key, '| zeros', zeros[key], '\n friends', friends[key])
    row, col, squared = friends[key]
    digits = zeros[key]
    pot1 = sum([zeros[k] for k in row], [])
    pot2 = sum([zeros[k] for k in col], [])
    pot3 = sum([zeros[k] for k in squared], [])
    found1 = list(filter(lambda x: pot1.count(x)==0, digits))
    found2 = list(filter(lambda x: pot2.count(x)==0, digits))
    found3 = list(filter(lambda x: pot3.count(x)==0, digits))
    found = max(found1, found2, found3)
    if len(found) > 1: # for backward to previous version pzl
        return []
    elif len(found) == 1:
=======
        if len(found) > 1: # for backward to previous version pzl
            return []
        elif len(found) == 1:
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
        if len(found) > 1: # for backward to previous version pzl
            return []
        elif len(found) == 1:
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
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
<<<<<<< HEAD
<<<<<<< HEAD
print('\npuzzle\n')
answer, zeros = sudoku_solver(puzzle)
print(np.array(answer))
print(answer == solution)

print('\npuzzle_hard\n')
<<<<<<< HEAD
answer = sudoku_solver(puzzle_hard)
=======
answer, zeros = sudoku_solver(puzzle)
print(np.array(answer))
print(answer == solution)

=======
answer, zeros = sudoku_solver(puzzle)
print(np.array(answer))
print(answer == solution)

>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
answer, zeros = sudoku_solver(puzzle_hard)
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
answer, zeros = sudoku_solver(puzzle_hard)
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
print(np.array(answer))
print(answer == solution_hard)

<<<<<<< HEAD
<<<<<<< HEAD
print('\ntest\n')
<<<<<<< HEAD
answer = sudoku_solver(test)
=======
=======
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
answer, snapshots = sudoku_solver(test)
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
answer, snapshots = sudoku_solver(test)
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
print(np.array(answer))
print(answer == solution_hard)

<<<<<<< HEAD
<<<<<<< HEAD
print('\nincorrect1\n')
<<<<<<< HEAD
answer = sudoku_solver(puzzle_inc)
=======
=======
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
answer, snapshots = sudoku_solver(puzzle_inc)
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
answer, snapshots = sudoku_solver(puzzle_inc)
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
print(np.array(answer))
print(answer == solution_hard)

<<<<<<< HEAD
<<<<<<< HEAD
print('\nincorrect2\n')
<<<<<<< HEAD
answer = sudoku_solver(puzzle_inc2)
=======
=======
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
answer, snapshots = sudoku_solver(puzzle_inc2)
>>>>>>> parent of cee1d7a... Update sudoku_very_hard.py
=======
answer, snapshots = sudoku_solver(puzzle_inc2)
>>>>>>> parent of 2e4fedb... Update sudoku_very_hard.py
print(np.array(answer))
print(answer == solution_hard)


end = time()
print('time ', end - start)
izm.append(end - start)