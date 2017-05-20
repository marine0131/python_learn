from sanitize import sanitize

def get_coach_data(filename):
    try:
        with open( filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ierr:
        print('file error:'+ str(ioerr))
        return None
               
james = get_coach_data('data/james2.txt')
julie = get_coach_data('data/julie2.txt')
mikey = get_coach_data('data/mikey2.txt')
sarah = get_coach_data('data/sarah2.txt')

print(james)
print(julie)
print(mikey)
print(sarah)
print('\n')
(james_name,james_bob) = (james.pop(0),james.pop(0))
(julie_name,julie_bob) = (julie.pop(0),julie.pop(0))
(mikey_name,mikey_bob) = (mikey.pop(0),mikey.pop(0))
(sarah_name,sarah_bob) = (sarah.pop(0),sarah.pop(0))
james_sort = sorted(set([sanitize(each_s) for each_s in james]))
julie_sort = sorted(set([sanitize(each_s) for each_s in julie]))
mikey_sort = sorted(set([sanitize(each_s) for each_s in mikey]))
sarah_sort = sorted(set([sanitize(each_s) for each_s in sarah]))

print(james_name + ':' + str(james_sort[0:3]))
print(julie_name + ':' + str(julie_sort[0:3]))
print(mikey_name + ':' + str(mikey_sort[0:3]))
print(sarah_name + ':' + str(sarah_sort[0:3]))
