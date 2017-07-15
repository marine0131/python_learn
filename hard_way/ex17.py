def copy_file(src_file, dst_file):
    print("copying from %r to %r" %(src_file, dst_file))
    src = open(src_file,'r')
    data = src.read()

    dst = open(dst_file, 'w')
    dst.write(data)
    
copy_file('ex17_1.txt','ex17_2.txt')
