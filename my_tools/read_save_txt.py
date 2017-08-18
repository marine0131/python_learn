#! use/bin/env python

import os
import linecache # read file over 1G

def read_and_split(rd_file,wt_file):
    with open(rd_file) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split(':')[0].strip())

    with open(wt_file,'w') as wf:
        for i in data:
            wf.write(i+',')


if __name__ == '__main__':
    read_and_split('old.txt','new.txt')
