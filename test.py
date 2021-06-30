#!/usr/bin/env python
# -*- coding:utf-8 -*-

import functools

my_list = [1, 2, 3, 4, 5]

# def f(x1, x2):
#     return x1 + x2


result = functools.reduce(lambda x, y: x + y, my_list)
result2 = map(lambda x: x * 2, my_list)
print(result2)
print(list(result2))
