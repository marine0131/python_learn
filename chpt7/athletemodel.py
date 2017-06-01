import pickle
from sanitize import sanitize
from athlete import Athlete

def get_coach_data(filename):
    try:
        with open( filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
        return(Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ierr:
        print('file error:'+ str(ioerr))
        return None

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath

james = get_coach_data('data/james2.txt')
julie = get_coach_data('data/julie2.txt')
mikey = get_coach_data('data/mikey2.txt')
sarah = get_coach_data('data/sarah2.txt')
