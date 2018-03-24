#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Hung
'''

import sys
import math

temperature_sum = 0.0
pressure_sum = 0.0
count = 0.0
temperature_avg = 3.02812018246
pressure_avg = 2257.852058
# input comes from STDIN (standard input)
# f = open("yhtest.csv",'r')
# for line in f:
for line in sys.stdin:
    count += 1
    # split file into line
    line = line.strip()
    # split the line into data
    data = line.split(',')
    if len(data[1]) == 0 or len(data[2]) == 0:
        count += -1
        continue
    # add up
    temperature_sum += math.pow(float(data[2])-temperature_avg, 2)
    pressure_sum += math.pow(float(data[1])-pressure_avg, 2)

print('temperature_sum\t%s\t%s' % (temperature_sum, count))
print('pressure_sum\t%s\t%s' % (pressure_sum, count))

