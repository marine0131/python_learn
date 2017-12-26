#! /usr/bin/env python

from bottle import route, run , request

@route('/')
def hello():
    return "hello world"

run(host='127.0.0.1', port=8080)
