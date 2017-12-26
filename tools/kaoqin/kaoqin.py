#! /usr/bin/env python

import sys
import os
import json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please input a file')
    file_name = sys.argv[1]
    file_name = os.path.join(os.path.abspath('.'), file_name)
    with open(file_name, 'r') as f:
        a_dict = json.load(f)
    print(a_dict)

    for name in a_dict:
        hours = a_dict[name]['hours']
        this_month_holiday = a_dict[name]['holiday']

        i = 0
        hours.append(a_dict[name]['new_month'])
        new_hours = hours.copy()

        while this_month_holiday > 0:
            if hours[i] >= this_month_holiday:
                new_hours[i] = hours[i] - this_month_holiday
                this_month_holiday = 0
                break

            else:
                new_hours[i] = 0
                this_month_holiday = this_month_holiday - hours[i]

            i = i+1
            if i > len(hours) - 1:
                break

        total = sum(new_hours) - this_month_holiday
        a_dict[name]['hours'] = new_hours[1:]
        a_dict[name]['total'] = total
        a_dict[name]['new_month'] = 0
        a_dict[name]['holiday'] = 0

    new_filename = file_name.split('.')[0] + '_new' + '.txt'
    with open(new_filename, 'w') as f:
        json.dump(a_dict, f)
