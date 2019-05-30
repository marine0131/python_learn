#! /usr/bin/env python

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

register_openers()

datagen, headers = multipart_encode({"image": open("./cat-3.jpg", "rb"), "fileId":"02a0bbcaba434d238c6d31a851f136dc"})
request = urllib2.Request("http://192.168.10.170/uploadDetectedImage.do", datagen, headers)

print(urllib2.urlopen(request).read())
