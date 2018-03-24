#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Hung
'''

import sys

temperature_avg = 3.02812018246
pressure_avg = 2257.852058
temperature_sd = 0.194243112075
pressure_sd = 12.4024286882
# input comes from STDIN (standard input)
# f = open("yhtest.csv",'r')
# for line in f:
for line in sys.stdin:
    # split file into line
    line = line.strip()
    # split the line into data
    data = line.split(',')
    # add up
    if len(data[1]) == 0 or len(data[2]) == 0:
        continue
    temperature = float(data[2])
    pressure = float(data[1])
    if abs(temperature - temperature_avg) > 3.0 * temperature_sd:
        print('temperature_outliers\t%s' % (temperature,))
    if abs(pressure - pressure_avg) > 3.0 * pressure_sd:
        print('pressure_outliers\t%s' % (pressure,))

