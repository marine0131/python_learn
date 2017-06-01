from sanitize import sanitize
from athlete import Athlete

#    def add_time(self, time):
#        self.times.append(time)
#    def add_times(self, times):
#        self.times.extend(times)
    
def get_coach_data(filename):
    try:
        with open( filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
        return(Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ierr:
        print('file error:'+ str(ioerr))
        return None

james = get_coach_data('data/james2.txt')
julie = get_coach_data('data/julie2.txt')
mikey = get_coach_data('data/mikey2.txt')
sarah = get_coach_data('data/sarah2.txt')

print(james.name+', '+james.dob+', '+'fastest times are:'+ str(james.pop3()))
print(julie.name+', '+julie.dob+', '+'fastest times are:'+ str(julie.pop3()))
print(mikey.name+', '+mikey.dob+', '+'fastest times are:'+ str(mikey.pop3()))
print(sarah.name+', '+sarah.dob+', '+'fastest times are:'+ str(sarah.pop3()))
