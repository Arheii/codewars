# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:27:21 2020

@author: Arh
"""
# Way1
def fib_din(n):
    """ work 20s for 10 ^ 6 """
    f0, f1 = 0, 1

    for _ in range(n - 1):
        f1, f0 = f0 + f1, f1
        
    if n < 1:
        return f0
    return f1


#  Way2
import numpy as np

def exp(n, X, I):
    """ return X ^ n , recursive"""
    if n == 0:
        return I
    if n == 1:
        return X
    Y = exp(n // 2, X, I)
    Y = mult(Y, Y)
    if n % 2:
        Y = mult(X, Y)
    return Y
    

def mult(A, B):
    """ 2x2 matrix multiply """
    AB = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            AB[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] 
    return AB


def fib(n):
    """ calculate used [[1, 1], [1, 0]] ** n == [[fib(n+1), fib(n)], [fib(n), fib(n-1)]]
    https://habr.com/ru/post/261159/
    numpy dont work
    """
    if n == 0:
        return 0
    if abs(n) == 1:
        return n
    I = [[1, 1], [1, 1]]
    X = [[1, 1], [1, 0]]
    fib_x = exp(abs(n) - 1, X, I)[0][0]
    if n < 0 and not n % 2:
        fib_x = -fib_x
    return int(fib_x)

    


#print(fib_din(4000))
print(fib(1000000))