#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Hung
'''

import sys

temperature_outliers_count = 0.0
pressure_outliers_count = 0.0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split file into line
    line = line.strip()
    # split the line into data
    key,value = line.split('\t')
    # add up
    if key == 'temperature_outliers':
        temperature_outliers_count += 1
    elif key == 'pressure_outliers':
        pressure_outliers_count += 1


print("temperature_outliers_count:%s" % (temperature_outliers_count,))
print("pressure_outliers_count:%s" % (pressure_outliers_count,))

