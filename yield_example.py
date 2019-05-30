#! /usr/bin/env python

import numpy as np
from operator import itemgetter


# a =np.array([ 877,  326, 942, 422])
# b =np.array([ 508, 348, 577, 418])
# c =np.array([ 684, 357, 755, 428])
#
#
# al = []
# al.append((a,'red'))
# al.append((b,'green'))
# al.append((c,'yellow'))
#
# al = sorted(al, key = lambda x: x[0][1])
# print map(lambda x: x[0][0]-500, al)
# print al
def simple_yield():
    print('aaaa')
    yield 5
    print('bbbb')
    yield 6
    print('cccc')

def yield_send():
    x = 1
    while True:
        y = yield x
        x += y

def square():
    for x in range(4):
        yield x ** 2

if __name__ == "__main__":
    gen = simple_yield()
    print(gen.next())
    print(gen.next())

    gen2 = yield_send()
    print(gen2.next())
    print(gen2.send(3)) # y is assigned 3
    print(gen2.send(6)) # y is assigned 6
    # square_gen = square()
    # print(square_gen.next())
    # print(square_gen.next())
