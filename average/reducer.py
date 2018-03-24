#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Hung
'''

import sys

value_sum =0.0
# temperature_sum = 0.0
# pressure_sum = 0.0
count = 0.0
# input comes from STDIN (standard input)
for line in sys.stdin:
    count += 1
    # split file into line
    line = line.strip()
    # split the line into data
    key,value = line.split('\t')
    # add up
    value_sum += float(value)


print("average:%s" % (value_sum/count,))
# print('temperature_average\t%s' % (temperature_sum/count,))
# print('pressure_average\t%s' % (pressure_sum/count,))

