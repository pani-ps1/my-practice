# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:29:05 2020

@author: utob
"""

name = "some thing really long"

if len(name) < 3:
    print("name must be at least 3 characters")
elif len (name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good!")
    