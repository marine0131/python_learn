try:
    with open('/home/whj/python_ws/chpt5/james.txt','r') as jaf:
        data = jaf.readline()
        james = data.strip().split(',')
    with open('/home/whj/python_ws/chpt5/julie.txt','r') as juf:
        data = juf.readline()
        julie = data.strip().split(',')
    with open('/home/whj/python_ws/chpt5/mikey.txt','r') as mif:
        data = mif.readline()
        mikey = data.strip().split(',')
    with open('/home/whj/python_ws/chpt5/sarah.txt','r') as saf:
        data = saf.readline()
        sarah = data.strip().split(',')
    print(james)
    print(julie)
    print(mikey)
    print(sarah)
except IOError as err:
    print('file err: ' + str(err))
