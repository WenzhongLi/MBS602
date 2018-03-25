#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

from mrjob.job import MRJob
import sys
import math


class StandardDeviation(MRJob):
    def mapper_init(self):
        f = open("/Users/wenzhongli/PycharmProjects/MBS602/MJresult.txt", 'r').readlines()
        f = f[::-1]
        for i in range(2):
            data = f[i].rstrip().split(':')
            if data[0] == "temperature_average":
                self.temperature_average = float(data[1])
            elif data[0] == "pressure_average":
                self.pressure_average = float(data[1])

    def mapper(self,key,line):
        temperature_sum = 0.0
        pressure_sum = 0.0
        count = 0.0
        temperature_avg = self.temperature_average
        pressure_avg = self.pressure_average

        for i, line in enumerate(line.split('/n')):
            count += 1
            # split file into line
            line = line.strip()
            # split the line into data
            data = line.split(',')
            if len(data[1]) == 0 or len(data[2]) == 0:
                count += -1
                continue
            # add up
            temperature_sum += math.pow(float(data[2]) - temperature_avg, 2)
            pressure_sum += math.pow(float(data[1]) - pressure_avg, 2)

        yield ("temperature_sum", str(temperature_sum)+","+str(count))
        yield ("pressure_sum", str(pressure_sum)+","+str(count))

    def reducer_init(self):
        self.temperature_standard_deviation = 0.0
        self.pressure_standard_deviation = 0.0

    def reducer(self,key,occurrences):
        temperature_sum = 0.0
        pressure_sum = 0.0
        temperature_count = 0.0
        pressure_count = 0.0

        # input comes from STDIN (standard input)
        for i, element in enumerate(occurrences):
            # split file into line
            value1, value2 = element.strip().split(',')
            # split the line into data
            # add up
            if key == 'temperature_sum':
                temperature_sum += float(value1)
                temperature_count += float(value2)
            elif key == 'pressure_sum':
                pressure_sum += float(value1)
                pressure_count += float(value2)
        if temperature_count != 0:
            yield ("temperature_standard_deviation", math.sqrt(temperature_sum / temperature_count))
            self.temperature_standard_deviation = math.sqrt(temperature_sum / temperature_count)
        if pressure_count != 0:
            yield ("pressure_standard_deviation", math.sqrt(pressure_sum / pressure_count))
            self.pressure_standard_deviation = math.sqrt(pressure_sum / pressure_count)

    def reducer_final(self):
        f = open("/Users/wenzhongli/PycharmProjects/MBS602/MJresult.txt",'a')
        if self.temperature_standard_deviation != 0:
            f.write("temperature_standard_deviation:"+str(self.temperature_standard_deviation)+"\n")
        if self.pressure_standard_deviation != 0:
            f.write("pressure_standard_deviation:"+str(self.pressure_standard_deviation)+"\n")
        f.flush()
        f.close()


if __name__ == '__main__':
    StandardDeviation.run()
    # print(r.temperature_average, r.pressure_average)