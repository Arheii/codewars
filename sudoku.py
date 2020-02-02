# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:42:33 2020
solve sudoku

kata3
https://www.codewars.com/kata/5296bc77afba8baa690002d
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

import numpy as np
#import heapq
def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    pzl = np.array(puzzle)
    zeros = 1
    while zeros:
        zeros = 0
        for i in range(9):
            for j in range(9):
                if pzl[i,j] == 0:
                    zeros += 1
                    new = check_cell(pzl, i, j)
                    if new:
                        pzl[i,j] = new
                        zeros -= 1
    return pzl.tolist()


def check_cell(pzl, n, m):
    digits = [x for x in range(1, 10) if x not in pzl[n,:]]
    if len(digits) == 1:
        return digits[0]
    digits = [x for x in digits if x not in pzl[:,m]]
    if len(digits) == 1:
        return digits[0]
    square = pzl[3 * (n // 3):3 * (n // 3) + 3, 3 * (m // 3): 3 * (m // 3) + 3]
    digits = [x for x in digits if x not in square.flat]
    if len(digits) == 1:
        return digits[0]
    return 0

    
    
print(sudoku(puzzle))

print(sudoku(puzzle) == solution)