#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

from mrjob.job import MRJob
import sys
import math


class Outlier(MRJob):
    def mapper_init(self):
        f = open("/home/yh608/homework2/MBS602/MJresult.txt", 'r').readlines()
        f = f[::-1]
        for i in range(4):
            data = f[i].rstrip().split(':')
            if data[0] == "temperature_average":
                self.temperature_average = float(data[1])
            elif data[0] == "pressure_average":
                self.pressure_average = float(data[1])
            elif data[0] == "temperature_standard_deviation":
                self.temperature_standard_deviation = float(data[1])
            elif data[0] == "pressure_standard_deviation":
                self.pressure_standard_deviation = float(data[1])

    def mapper(self,key,line):
        temperature_avg = self.temperature_average
        pressure_avg = self.pressure_average
        temperature_sd = self.temperature_standard_deviation
        pressure_sd = self.pressure_standard_deviation
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
                yield('temperature_outliers', temperature)
            if abs(pressure - pressure_avg) > 3.0 * pressure_sd:
                yield('pressure_outliers', pressure)

    def reducer_init(self):
        self.temperature_outliers_count = -1.0
        self.pressure_outliers_count = -1.0

    def reducer(self,key,occurrences):
        temperature_outliers_count = 0.0
        pressure_outliers_count = 0.0
        if key == 'temperature_outliers':
            temperature_outliers_count = len(occurrences)
            yield ("temperature_outliers_count", temperature_outliers_count)
            self.temperature_outliers_count = temperature_outliers_count
        elif key == 'pressure_outliers':
            pressure_outliers_count = len(occurrences)
            yield ("pressure_outliers_count", pressure_outliers_count)
            self.pressure_outliers_count = pressure_outliers_count

    def reducer_final(self):
        f = open("/home/yh608/homework2/MBS602/MJresult.txt",'a')

        if self.temperature_outliers_count != -1:
            f.write("temperature_outliers_count:"+str(self.temperature_outliers_count)+"\n")
        if self.pressure_outliers_count != -1:
            f.write("pressure_outliers_count:"+str(self.pressure_outliers_count)+"\n")
        f.flush()
        f.close()


if __name__ == '__main__':
    Outlier.run()