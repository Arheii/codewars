# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:12:35 2020
Возвращается следующее простое число до миллиона
Тестирую чтобы вникнуть в класс/статикметод
kata 3
https://www.codewars.com/kata/prime-streaming-pg-13/
@author: Arh
"""
import time
class Primes:
    @staticmethod
    def stream():
        N = 18000000
        n = (N) // 2
        smpl = [True] *  n
        for i in range(0, int(n ** 0.5)):
            if smpl[i]:
                for j in range(((2 * i + 3) ** 2 - 3) // 2, n, 2 * i + 3):
                    smpl[j] = False
        
#        print(smpl[:20])

        yield 2
        for i in range(n):
            if smpl[i]:
                yield i * 2 + 3
#        n = N
#        smpl = [True] * n
#        for i in range(2, int(n ** 0.5)):
#            if smpl[i]:
#                for j in range(2 * i, n, i):
#                    smpl[j] = False
#        
#        print(smpl[:20])            
#        for i in range(2, n):
#            if smpl[i]:
#                yield i
                
start = time.time()            
g = Primes.stream()
next(g)
end = time.time()
print('[*] Время выполнения: {} секунд.'.format(end-start))

for i in range(1000000):
    it = i
    next(g)
#print(next(g))
end2 = time.time()
print('[*] Время цикла миллиона: {} секунд.'.format(end2-end))