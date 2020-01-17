# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:59:42 2020
Compute time to crash trains
kata 2
https://www.codewars.com/kata/59b47ff18bcb77a4d1000076/train/python   
@author: Arh
"""

import time
from itertools import product

TRACK_EX = """\
                                /------------\\
/-------------\\                /             |
|             |               /              S
|             |              /               |
|        /----+--------------+------\\        |   
\\       /     |              |      |        |     
 \\      |     \\              |      |        |                    
 |      |      \\-------------+------+--------+---\\
 |      |                    |      |        |   |
 \\------+--------------------+------/        /   |
        |                    |              /    | 
        \\------S-------------+-------------/     |
                             |                   |
/-------------\\              |                   |
|             |              |             /-----+----\\
|             |              |             |     |     \\
\\-------------+--------------+-----S-------+-----/      \\
              |              |             |             \\
              |              |             |             |
              |              \\-------------+-------------/
              |                            |               
              \\----------------------------/ 
"""
RABBIT = """\
    /---------------------\\               /-\\ /-\\  
   //---------------------\\\\              | | | |  
  //  /-------------------\\\\\\             | / | /  
  ||  |/------------------\\\\\\\\            |/  |/   
  ||  ||                   \\\\\\\\           ||  ||   
  \\\\  ||                   | \\\\\\          ||  ||   
   \\\\-//                   | || \\---------/\\--/|   
/-\\ \\-/                    \\-/|                |   
|  \\--------------------------/                |   
\\----------------------------------------------/ 
"""

def print_track(track, a_train, b_train, a_name, b_name):
    """ print track with trains for debug"""
    for i in range(len(track)):
        for j in range(len(track[i])):
            if track[i][j] != ' ':
                if [i, j] in a_train:
                    ch = a_name
                    if [i, j] == a_train[0]:
                        ch = a_name.upper()
                elif [i, j] in b_train:
                    ch = b_name
                    if [i, j] == b_train[0]:
                        ch = b_name.upper()
                else:
                    ch = track[i][j]
                    
                print(ch, end='')
                    
            else:
                print(' ', end='')
        print()


def gen_coords(track, old, cur):
    """ return next coords track """
    while True:
        x, y = [i + (i - j) for i, j in zip(cur, old)]
        if track[x][y] != ' ':    # check next in line
            old, cur = cur, [x, y]
            # situation   /
            #           --+-
            if track[old[0]][old[1]] == '\\'  or track[old[0]][old[1]] == '/':
                if track[x][y] == '-':
                    if track[x][y + 1] == '+':
                        cur = [x, y + 1]
                    if track[x][y - 1] == '+':
                        cur = [x, y - 1]
        else:                               # check other 4 invariants
            dif = [i - j for i, j in zip(cur, old)]
            if 0 in dif:
                dx, dy = [[i, i + j] if j else [i - 1, i + 1] for i, j in zip(cur, dif)]
                koords = product(dx, dy)
            else:
                dx, dy = dif
                koords = [[x, y - dy], [x, y - 2 * dy], [x - dx, y], [x - 2 * dx, y]]
                
            for x, y in koords:
                if track[x][y] != ' ':
                    old, cur = cur, [x, y]
            
        yield cur
        

class Train():
    def __init__(self, train, train_pos, track, zero_pos):
        """Constructor trains"""
        self.name = train[0].lower()
        self.track = track
        self.n = len(train)
        self.expr = (self.name == 'x')
        self.delay = 0
        self.clockwise = train[-1].isupper()
        self.train = self._move_to_start(train_pos, zero_pos)
        self.move = gen_coords(self.track, self.train[1], self.train[0])

            
    def _move_to_start(self, train_pos, zero_pos):
        """Move all train to start positions and return train"""
        g =  gen_coords(self.track, [1, zero_pos - 1], [1, zero_pos])
        for i in range(train_pos - 1):
            next(g)            
        engine = next(g)
        train = [engine]
        if self.clockwise: 
            g = gen_coords(self.track, next(g), engine) 
        for i in range(1, self.n):
            train.append(next(g))
                
        return train

        
    def tuh_tuh(self):
        if self.delay:
            self.delay -= 1
            return 
        
        self.train[1:] = self.train[:-1]
        self.train[0] = x, y = next(self.move)
        if not self.expr and self.track[x][y] == 'S':
            self.delay = self.n - 1        
        return 


def check_start_crash(a_train, b_train):
    for a in a_train:
        if a_train.count(a) > 1 or a in b_train:
            return True
    for b in b_train:
        if b_train.count(b) > 1 or b in a_train:
            return True
    return False


def crash(a_train, b_train):
    if a_train[0] in b_train or b_train[0] in a_train:
        return True
    else:
        return False


def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):
    track = track.split('\n')
    maxl = max([len(line) for line in track]) + 1
    track = [' ' + line + ' ' * (maxl - len(line)) for line in track]
    track.insert(0, " " * len(track[0]))
    track.append(" " * len(track[1]))   
    zero_pos = track[1].find('/')  
    
    A = Train(a_train, a_train_pos, track, zero_pos)
    B = Train(b_train, b_train_pos, track, zero_pos)
    if check_start_crash(A.train, B.train):
        return  0
    print_track(track, A.train, B.train, A.name, B.name)
    for i in range(1, limit + 1):
        A.tuh_tuh()
        B.tuh_tuh()
#        if i == 185:
        print_track(track, A.train, B.train, A.name, B.name)
        if crash(A.train, B.train):
            print_track(track, A.train, B.train, A.name, B.name)
            return i

        time.sleep(1)
        
    return 0

#print(train_crash(TRACK_EX, "Aaaa", 147, "Bbbbbbbbbbb", 288, 1000))
#print(train_crash(TRACK_EX, "Xxxxxxx", 115, "Cccc", 146, 1000))
print(train_crash(RABBIT, "ddddddddddD", 10, "Xxxxx", 162, 1000))