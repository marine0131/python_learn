#! /usr/bin/env python

import os

def convertFileToOneAndZero(path):
    with open(path, 'rb') as f:
        src = f.read()

    result = []
    for i in src:
        temp = bin(ord(i))[2:]
        temp = '0' * (8-len(temp)) + temp
        result.append(temp)

    return ''.join(result)

# src: 101001 string
# path: path save the output file
def convertOneAndZeroToFile(src, path):
    result = []
    for i in range(0, len(src), 8):
        result.append(chr(int(src[i:i+8], 2)))

    with open(path, 'wb') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    input_path = '/home/whj/1.bag'
    output_path = '/home/whj/2.bag'
    print 'input file size:{}'.format(os.path.getsize(input_path))
    bi = convertFileToOneAndZero(input_path)
    convertOneAndZeroToFile(bi, output_path)
    print 'output file size:{}'.format(os.path.getsize(output_path))

