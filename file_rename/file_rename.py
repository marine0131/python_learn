#!/usr/bin/env python
import os


def file_rename(src_dir, dst_dir, prefix):
    
    raw_names=[]
    for raw_name in os.listdir(src_dir):
        raw_names.append(raw_name)  
    raw_names.sort()
    num=0
    for name in raw_names:
        src = src_dir + name
        dst = dst_dir + prefix + str(num).zfill(4) +'.jpg'
        print(src,'-->',dst)
        os.rename(src,dst)
        num=num+1
        
if __name__ == '__main__':
    src_dir='pic/'
    dst_dir='pic/'
    prefix='pic'
    file_rename(src_dir,dst_dir,prefix)
