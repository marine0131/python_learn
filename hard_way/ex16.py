def ex16(filename):

    print ("opening file...")
    target = open(filename, 'r+')
    print("here's content")
    print(target.read())
    target.close()
    
    print ("if you want to erase %r." %filename)
    print ("if you don't want that, hit ctrl+c")
    print ("if you do want that, hit return")
    input("?")
    target = open(filename, 'w')
    print ("truncating the file, goodluck\n")
    target.truncate()

    print ("now you can print 3 new lines:")

    line1=input("1> ")
    line2=input("2> ")
    line3=input("3> ")

    print ("writing these to file...")
    target.write(line1)
    target.write('\n')
    target.write(line2)
    target.write('\n')
    target.write(line3)
    target.write('\n')

    print ("write complete")
    target.close()

ex16('ex16_.txt')
    
