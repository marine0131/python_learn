import pickle
try:
    with open('/home/whj/python_ws/mydata.txt','wb') as mysavedata:
        pickle.dump([1,2,3,'four'],mysavedata)

    with open('/home/whj/python_ws/mydata.txt','rb') as myrestoredata:
        a_list = pickle.load(myrestoredata)

    print(a_list)

except IOError as err:
    print('file error: '+str(err))

except pickle.PickleError as perr:
    print('pickle error'+ str(perr))
