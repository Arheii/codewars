# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:12:35 2020
Возвращается следующее простое число до миллиона
Тестирую чтобы вникнуть в класс/статикметод
kata 3
https://www.codewars.com/kata/prime-streaming-pg-13/
@author: Arh
"""

import numpy as np
import time

class Primes:
    @staticmethod
    def stream():
        """
        return next first number
        + unlimited
        + spends less memory and time for small primes (than other solutions)
        - disgusting code
        """
        def add_primes():
            """ looking for prime numbers in the range of (board - r_bard)"""
            nonlocal primes, board
            right_b = int(board * 1.1)
            if right_b % 2: right_b += 1
            n = (right_b - board) // 2
            smpl = np.ones(n, dtype=np.bool)
            for x in primes:
                if x * x > right_b:
                    break
                ost = board % x
                if ost % 2:
                    start = (2 * x - ost - 1) // 2
                else:
                    start = (x - ost - 1) // 2
                smpl[start::x] = False             
            s = [board + i * 2 + 1 for i, k in enumerate(smpl) if k]
            primes.extend(s)
            board = right_b
            return len(s)
        
        board = 150000
        n = board // 2 - 1 
        smpl = np.ones(n, dtype=np.bool)
#        always looking for primes in the range [3 - 150001]
        for i in range(int(n ** 0.5)):
            if smpl[i]:
                smpl[((2 * i + 3) ** 2 - 3) // 2::2 * i + 3] = False
        primes = [i * 2 + 3 for i, k in enumerate(smpl) if k]
       
        yield 2
        i, len_primes = 0, len(primes)
        while True:
            if i == len_primes:
                len_primes += add_primes()
            yield primes[i]
            i += 1


    @staticmethod
    def stream_2():
        board = 18000000           

        n = board
        smpl = [True] * n
        for i in range(2, int(n ** 0.5)):
            if smpl[i]:
                for j in range(i ** 2, n, i):
                    smpl[j] = False
                   
        for i in range(2, n):
            if smpl[i]:
                yield i
                
start = time.time()    
g = Primes.stream()        
g2 = Primes.stream_2()
next(g)
next(g2)
end = time.time()
print('[*] Время выполнения: {} секунд.'.format(end-start))

for i in range(1000000):
    c, d = a, b
    a = next(g)
    b = next(g2)    
    if a != b:
        print('Fack', i, a, b, 'old', c, d)
        break
    
#print(next(g))
end2 = time.time()
print('[*] Время цикла миллиона: {} секунд.'.format(end2-end))