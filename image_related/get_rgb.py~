#! /usr/bin/env python

from PIL import Image

im = Image.open('abc.png')
pix = im.load()

width = im.size[0]
height = im.size[1]

rgb = []
for x in range(width):
    for y in range(height):
        rgb.append(pix[x, y])

with open('rgb.txt', 'w') as wf:
    for i in rgb:
        wf.write(str(i)+'\n')
