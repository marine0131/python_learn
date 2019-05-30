import struct
import os
import math
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped
from tf import TransformListener, transformations, Transformer

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


def returnlist(msg):
    return [msg.pose.position.x, msg.pose.position.y]

if __name__=='__main__':
    # rospy.init_node('test')
    # t = TransformListener()
    # # quat = transformations.quaternion_from_euler(0,0,math.pi/4)
    # quat = [0, 0, -0.73, 0.68344]
    # rot = TransformListener.fromTranslationRotation(t, translation=(0,0,0), rotation=(quat[0],quat[1],quat[2],quat[3]))
    # a = [1,0,0,1]
    # print np.dot(a,rot)[0:3] + [0.255, 0.3 ,0]
    print("lalalallala")
