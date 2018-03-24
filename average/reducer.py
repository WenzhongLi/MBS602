#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Hung
'''

import sys

value_sum =0.0
temperature_sum = 0.0
pressure_sum = 0.0
temperature_count = 0.0
pressure_count = 0.0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split file into line
    line = line.strip()
    # split the line into data
    key, value1, value2 = line.split('\t')
    # add up
    if key == 'temperature_sum':
        temperature_sum += float(value1)
        temperature_count += float(value2)
    elif key == 'pressure_sum':
        pressure_sum += float(value1)
        pressure_count += float(value2)


print("temperature_average:%s" % (temperature_sum/temperature_count,))
print("pressure_average:%s" % (pressure_sum/pressure_count,))
# print('temperature_average\t%s' % (temperature_sum/count,))
# print('pressure_average\t%s' % (pressure_sum/count,))

