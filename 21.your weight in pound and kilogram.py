# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:35:20 2020

@author: utob
"""

weight = int (input('weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print (f"you are {converted} pounds")
    