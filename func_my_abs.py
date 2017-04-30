#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

def my_abs(x=100):
    if not isinstance(x,(int,float)):
        raise TypeError('Type Error.')

    if x>0:
        return x
    elif x==0:
        pass
    else:
        return -x

print(my_abs(0),my_abs(1),my_abs(1))
print(my_abs())