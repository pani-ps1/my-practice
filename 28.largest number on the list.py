# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:44:00 2020

@author: utob
"""

numbers = [3, 6, 2, 8, 4, 10 ]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)