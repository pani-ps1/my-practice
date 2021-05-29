# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:43:43 2020

@author: utob
"""
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)