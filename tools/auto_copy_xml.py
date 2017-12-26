#! /usr/bin/env python

import os
import sys
import shutil

xml_path = '/home/liting/data_make/datamake/numxml/'
# xml_path = '/home/whj/'
[file_name, ext] = sys.argv[1].split('.')
num = int(sys.argv[2])
src_file = os.path.join(xml_path, file_name+'.'+ext)
dst_path = os.path.join(xml_path, 'generated')
if not os.path.exists(dst_path):
	os.mkdir(dst_path)

for i in range(num):
    new_name = "%06d" %(int(file_name)+i+1) + '.'+ext
    new_file = os.path.join(dst_path, new_name)
    print('copying {}'.format(new_name))
    shutil.copyfile(src_file, new_file)
