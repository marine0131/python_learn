import struct
import os
import math

def lower():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]

    print(L2)

def gen():
    L=[x*x for x in range(10)]
    print('list is:',L)
    g=(x*x for x in range(10))
    print('generation is:',g)  
    for gg in g:
        print(gg)

def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'

def writeFile():
    f = open('./new.txt','a')
    p={'x':12,'y':13,'z':14}
    q={'w':1,'x':1.2,'y':1.3,'z':1.5}
    z={'pose':p,'quat':q}
    f.write(str(z)+'\n')
    f.close()
    
    
if __name__=='__main__':
    writeFile()
