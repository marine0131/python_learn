from sanitize import sanitize

def get_coach_data(filename):
    try:
        with open( filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
        return({'Name':templ.pop(0),'DOB':templ.pop(0),'Times':sorted(set([sanitize(t) for t in templ]))})
    except IOError as ierr:
        print('file error:'+ str(ioerr))
        return None
               
james = get_coach_data('data/james2.txt')
julie = get_coach_data('data/julie2.txt')
mikey = get_coach_data('data/mikey2.txt')
sarah = get_coach_data('data/sarah2.txt')

print(james['Name']+', '+james['DOB']+', '+'fastest times are:'+ str(james['Times']))
print(julie['Name']+', '+julie['DOB']+', '+'fastest times are:'+ str(julie['Times']))
print(mikey['Name']+', '+mikey['DOB']+', '+'fastest times are:'+ str(mikey['Times']))
print(sarah['Name']+', '+sarah['DOB']+', '+'fastest times are:'+ str(sarah['Times']))
