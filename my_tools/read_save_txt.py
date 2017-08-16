#! use/bin/env python

import os
import linecache # read file over 1G

def read_and_split(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split(':')[0].strip())

    with open('newnew.txt','w') as wf:
        for i in data:
            wf.write(i+',')


if __name__ == '__main__':
    read_and_split('new.txt')
