#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:59:39 2017

@author: franco
"""

import ctypes as C
import numpy as np

mate = C.CDLL('./libmate.so')
intp = C.POINTER(C.c_int)
flp = C.POINTER(C.c_float)
n1 = 2
n2 = 5
n3 = 3

int_a = C.c_int(n1)
int_b = C.c_int(n2)
int_c = C.c_int()

fl_a = C.c_float(float(n1))
fl_b = C.c_float(float(n2))
fl_c = C.c_float()

arr_int_a = np.array([n1, n2, n3], dtype=C.c_int)
arr_int_b = np.array([n2, n3, n1], dtype=C.c_int)
arr_int_c = np.zeros(arr_int_a.shape[0], dtype=C.c_int)
m = C.c_int(arr_int_a.shape[0])

arr_fl_a = np.array([n1, n2, n3], dtype=C.c_float)
arr_fl_b = np.array([n2, n3, n1], dtype=C.c_float)

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

# Integer array sum
mate.add_int_array(arr_int_a.ctypes.data_as(intp), \
                   arr_int_b.ctypes.data_as(intp), \
                   arr_int_c.ctypes.data_as(intp), m)
print('add_int_array {}'.format(arr_int_c))

#Dot product
mate.dot_product.restype = C.c_float
c = mate.dot_product(arr_fl_a.ctypes.data_as(flp), \
                 arr_fl_b.ctypes.data_as(flp), m)
print('dot_product {}'.format(c))
