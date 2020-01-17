# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 23:11:41 2020
Возвращает индекс из сортированного списка анаграмм для заданного слова
не учитывает словарь 
"ABA" -> "AAB", "ABA", "BAA" -> 2
kata 3
https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python
@author: Arh
"""
import math
  
word = 'QUESTION'  

# Way 1
# work only without repeat symbols
# can be refactoring to full solution
ans = 0
lw = len(word)
word2 = list(word)
for i in range(lw):
    ans += math.factorial(lw - i - 1) * sorted(word2).index(word[i])
    word2.pop(0)
print(ans + 1)


# Way 2, Full
def rec_anagram(word):
    """ Return found position and  total positions for last symbols """       
    if not word:
        return 1, 1
    ch = word[0]
    found, total = rec_anagram(word[1:])        
    current = sorted(word).index(ch) * total // word.count(ch)
    return current + found, total * len(word) // word.count(ch)

print(rec_anagram(word)[0])
