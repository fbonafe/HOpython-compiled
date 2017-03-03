#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:59:39 2017

@author: franco
"""

import ctypes as C
mate = C.CDLL('./libmate.so')
n1 = 2
n2 = 5
int_a = C.c_int(n1)
int_b = C.c_int(n2)
int_c = C.c_int()
fl_a = C.c_float(float(n1))
fl_b = C.c_float(float(n2))
fl_c = C.c_float()

#arr_int_a = 
#arr_int_b = 
#arr_int_c = 
#n = 
#arr_fl_a = 
#arr_fl_b = 

#Integer sums
c = mate.add_int(int_a, int_b)
print('add_int {}'.format(c))
mate.add_int_ref(C.byref(int_a), C.byref(int_b), C.byref(int_c))
print('add_int_res {}'.format(int_c.value))

#Float sums
mate.add_float.restype = C.c_float
c = mate.add_float(fl_a, fl_b)
print('add_float {}'.format(c))
mate.add_float_ref(C.byref(fl_a), C.byref(fl_b), C.byref(fl_c))
print('add_float_res {}'.format(fl_c.value))
