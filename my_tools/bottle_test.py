#! /usr/bin/env python

from bottle import route, run, request
#192.168.10.162:2333/?image=home/whj/1.jpg&debug=true
@route('/')
def index():
    # request parameter
    image_dir = request.query.image
    debug = request.query.debug.upper()

    if debug == 'TRUE':
        dir_list = str(image_dir).split('/')
        if not dir_list[-1]:
            dir_list.pop()
        dir_list.pop()
        output_dir = '/'.join(dir_list)+'/'
        return output_dir

    return image_dir

run(host='192.168.10.162', port=2333)
