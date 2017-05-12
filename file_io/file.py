import nester

man = []
other = []
try:
    data = open('/home/whj/python_ws/sketch.txt')
    data.seek(0)
    for each_line in data:
        try:
            (role,line_spoken) =each_line.split(":",1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as err:
    print('file error: '+ str(err))

try:
    with open("/home/whj/python_ws/man.txt",'w') as man_file,open("/home/whj/python_ws/other.txt",'w') as other_file:
        nester.print_lol(man, fh = man_file)
        nester.print_lol(other,fh = other_file)
except IOError as err:
    print("file error" + str(err));

'''with open("/home/whj/python_ws/man.txt") as test:
    print(test.readline())
with open("/home/whj/python_ws/other.txt") as test1:
    print(test1.readline())'''

