#!/usr/bin/env python3
from functools import reduce

def map_func(x):
    return x*x

def map_example():
    raw_list=[1,2,3,4,5,6,7,8,9]
    r1=map(map_func, raw_list) #r is a iterator
    r2=map(str , raw_list)
    print(list(r1)) #need turn into list
    print(list(r2))

def reduce_func(x,y):
    return x*10+y

def reduce_example():
    l = [1,2,3,4,5,6,7,8,9]
    res = reduce(reduce_func,l)
    print(res)

def normalize(name):
    return name[0].upper()+name[1:].lower()
def exam1(names):
    n_names=map(normalize, names)
    print('output:',list(n_names))

def prod(x,y):
    return x*y
def exam2(l):
    print('output:', reduce(prod,l))

def str2float(s):
    def float_prod(x,y):
        global dot
        if x=='.':
            dot = 1
            return y
        if y =='.':
            dot = 0
            return x
        else:
            dot = dot + 1
            return x*10+y
    
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}[s]
    print(reduce(float_prod,list(map(char2num,s)))/pow(10,dot))
    
if __name__=='__main__':
    #map_example()
    #reduce_example()
    names=['adam', 'LISA', 'barT']
    print('exam1\ninput list:', names)
    exam1(names)
    
    l=[3,5,9,8,9,10]
    print('exam2\ninput number list:', l)
    exam2(l)
    
    dot=0
    while(True):
        print('input a float string:(type \'exit\' to stop)')
        s = input()
        if s == 'exit':
            break
        else:
            str2float(s)
        
    
    
    
