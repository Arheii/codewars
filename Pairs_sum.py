# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 03:32:45 2020
Return first two values, wich summ = summ
kata 5
https://www.codewars.com/kata/54d81488b981293527000c8f
@author: Arh
"""

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
l9= list(range(1000)) * 100

from bisect import bisect_left
def sum_pairs(ints, s):
    """ Реализация через сортированный список и bisect
    не проходит по времени"""
    lst = sorted((x,i) for i, x in enumerate(ints))
    pair = None
    sum_ind_pair = False
    stop_ind = len(ints)
    for i, x in enumerate(ints):
        if i == stop_ind:
            break
        j = bisect_left(lst, (s - x, 0))
        if j < stop_ind:
            if s-x != x and lst[j][0] == s-x:
                z = lst[j][1]
            elif s-x == x and lst[j+1][0] == x:
                z = lst[j+1][1]
            else:
                continue
            if z < stop_ind:
                stop_ind = z
                pair = [x, s - x]

    return pair


def sum_pairs_dict(ints, s):
    """ with Dasha help!!!"""
    A = set()
    for x in ints:
        if s-x in A:
            return [s-x, x]
        else:
            A.add(x)
    return None


#for l in [l1, l2, l3, l4, l5, l6, l7, l8]:
#    print(l, sum_pairs(ints, s))
    
#print('l9', sum_pairs(l9, -1))
print('l5', sum_pairs_dict(l5, 10))