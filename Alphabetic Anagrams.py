# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 23:11:41 2020
Возвращаем порядковый номер возмножной анаграммы из заданного слова
не учитывает словарь 
kata 3
https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python
@author: Arh
"""
import math
#def listPosition(word):
#    """Return the anagram list position of the word"""
#    chars = [ord(w) - ord(A) for w in word]
#    dict_chrs  = {set(chrs)
#    set_chrs = set(word)
#    dict_chrs = {set_chrs[i]: i + 1 for i in range(len(set_chrs))}
#    return 1
    
word = 'QUESTION'  
set_chrs = set(word)
dict_chrs = {ch:i for i, ch in enumerate(sorted(set(word)), 1)}

ans = 0
lw = len(word)
word2 = list(word)
for i in range(lw):
    ans += math.factorial(lw - i - 1) * sorted(word2).index(word[i])
    word2.pop(0)
print(ans + 1)

def rec_anagram(word):
    if not word:
        return 0, 1
    n, variative = rec_anagram(word[1:])    
    ind_ch = sorted(word).index(word[0]) * variative
    if word[0] in word[1:]:
        ind_ch //= word.count(word[0])
       
    print(word[0], ind_ch * variative, variative * len(word) // word.count(word[0]))
    return ind_ch + n, variative * len(word) // word.count(word[0])

print(rec_anagram(word)[0])
