#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:03:42 2022

@author: stoner69
"""

import time
def test_time():
    
    

    #input time
    time_ = int(input("Enter number of seconds the loop should run: "))
    t_end = time.time() + time_

    c=0

    while time.time() < t_end:
        c=c+1

    print(c)