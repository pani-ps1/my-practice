# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:48:33 2020

@author: utob
"""

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_pyment = 0.2 * price
print(f"down payment: {down_payment}")
     