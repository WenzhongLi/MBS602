#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

from mrjob.job import MRJob
import sys


class Average(MRJob):
    def reducer_init(self):
        self.temperature_average = 0.0
        self.pressure_average = 0.0

    def mapper(self,key,line):
        temperature_sum = 0.0
        pressure_sum = 0.0
        count = 0.0
        for i, line in enumerate(line.split('/n')):
            count += 1
            # split file into line
            line = line.strip()
            # split the line into data
            data = line.split(',')
            # add up
            if len(data[1]) == 0 or len(data[2]) == 0:
                count += -1
                continue
            temperature_sum += float(data[2])
            pressure_sum += float(data[1])
        yield ("temperature_sum", str(temperature_sum)+","+str(count))
        yield ("pressure_sum", str(pressure_sum)+","+str(count))

    def reducer(self,key,occurrences):
        temperature_sum = 0.0
        pressure_sum = 0.0
        temperature_count = 0.0
        pressure_count = 0.0
        for i, element in enumerate(occurrences):
            data = element.strip().split(',')
            if key == 'temperature_sum':
                temperature_sum += float(data[0])
                temperature_count += float(data[1])
            elif key == 'pressure_sum':
                pressure_sum += float(data[0])
                pressure_count += float(data[1])
        if temperature_count != 0:
            yield ("temperature_average", temperature_sum/temperature_count)
            self.temperature_average = temperature_sum / temperature_count
        if pressure_count != 0:
            yield ("pressure_average", pressure_sum/pressure_count)
            self.pressure_average = pressure_sum / pressure_count

    def reducer_final(self):
        f = open("/home/yh608/homework2/MBS602/MJresult.txt",'a')
        if self.temperature_average != 0:
            f.write("temperature_average:"+str(self.temperature_average)+"\n")
        if self.pressure_average != 0:
            f.write("pressure_average:"+str(self.pressure_average)+"\n")
        f.flush()
        f.close()


if __name__ == '__main__':
    Average.run()
    # print(r.temperature_average, r.pressure_average)