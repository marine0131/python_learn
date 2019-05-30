#! /usr/bin/env python


import os
import subprocess as sp

sp.call('ip route list > ./ipout' , shell=True)

route = []
with open("./ipout") as f:
    for ll in f.readlines():
        route.append(ll.split(' '))

print route
if len(route) > 2 and route[0][4]=='eth0':
    # get ppp0 dev but default is not ppp0
    print "set ppp0 as default"
    sp.call('sudo ip route change to default dev ppp0', shell=True)

elif len(route) <= 2:
    # ppp0 dev not found
    print "restart ppp startup.sh"
    sp.call('sudo sh /etc/ppp/startup.sh')
