#! /usr/bin/env python

from PIL import Image
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'please input 1:dir 2:source ext 3:dest ext'
    else:
        image_path = os.path.join(os.curdir, sys.argv[1])

    src_ext = '.' + sys.argv[2]
    dst_ext = '.' + sys.argv[3]
    for image in os.listdir(image_path):
        tt = os.path.splitext(image)
        if tt[1] == src_ext:
            dst_image = os.path.join(image_path, tt[0] + dst_ext)
            print 'convert:' + image + '==>' + dst_image
            try:
                Image.open(os.path.join(image_path, image)).save(dst_image)
            except Exception as e:
                print e
