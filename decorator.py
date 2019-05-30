import logging
'''
use_logging is a function decorator
'''
def func_deco(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)

    return wrapper

@func_deco
def bar():
    print("i am bar")

@func_deco
def foo():
    print("i am foo")

'''
Deco is a class decorator
'''
class ClassDeco(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator running')
        self._func()
        print('class decorator ending')
@ClassDeco
def gee():
    print('gee')

gee()
