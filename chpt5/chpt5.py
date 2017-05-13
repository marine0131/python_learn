from sanitize import sanitize
def get_coach_data(filename):
    try:
        with open( filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ierr:
        print('file error:'+ str(ioerr))
        return None
               
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(james)
print(julie)
print(mikey)
print(sarah)
print('\n')

james_sort = sorted([sanitize(each_s) for each_s in james])
julie_sort = sorted([sanitize(each_s) for each_s in julie])
mikey_sort = sorted([sanitize(each_s) for each_s in mikey])
sarah_sort = sorted([sanitize(each_s) for each_s in sarah])

james_unique = []
julie_unique = []
mikey_unique = []
sarah_unique = []
for each_s in james_sort:
    if each_s not in james_unique:
        james_unique.append(each_s)
        
for each_s in julie_sort:
    if each_s not in julie_unique:
        julie_unique.append(each_s)
        
for each_s in mikey_sort:
    if each_s not in mikey_unique:
        mikey_unique.append(each_s)
        
for each_s in sarah_sort:
    if each_s not in sarah_unique:
        sarah_unique.append(each_s)


print(james_unique[0:3])
print(julie_unique[0:3])
print(mikey_unique[0:3])
print(sarah_unique[0:3])
