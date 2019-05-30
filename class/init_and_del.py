#! /usr/bin/env python

import time
class Test():
    def __init__(self):
        print("init class")

    def __del__(self):
        print("delete")


t = Test()
while True:
    print("running")
    time.sleep(1)
