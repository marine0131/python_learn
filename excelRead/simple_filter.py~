#! /usr/bin/env python
from xlrd import open_workbook
import xlwt
from xlutils.copy import copy


# get median data
def median(m_list):
    m_list = sorted(m_list)
    l = len(m_list)
    if l % 2 == 1:
        return m_list[l / 2]
    else:
        return (m_list[l/2-1]+m_list[l/2])/2


# filter
def simple_filter(t_list, th):
    del_list = []
    me = median(t_list)
    l = len(t_list)
    for i in range(l-1, -1, -1):
        # if i == l-1:
        #    if abs(t_list[i] - t_list[i-1]) > th:
        #        del_list.append([i,t_list[i]])
        #        t_list.pop(i)
        if i == 0:
            if abs(t_list[i] - t_list[i+1]) > th:
                del_list.append([i, t_list[i]])
                t_list.pop(i)
        else:
            if abs(t_list[i] - t_list[i-1]) > th:  # abs(t_list[i] - t_list[i-1]) > th or abs(t_list[i] - t_list[i+1]) > th:
                j = i if abs(t_list[i] - me) > abs(t_list[i-1] - me) else i-1
                del_list.append([j, t_list[j]])
                t_list.pop(j)

    return t_list, del_list


if __name__ == '__main__':
    # read excel data
    wb = open_workbook('data.xlsx')
    sh1 = wb.sheets()[0]
    col = sh1.col_values(6)[1:]

    # filter
    data, del_list = simple_filter(col, 10)
    print del_list

    # save to excel data
    wwb = copy(wb)
    sh = wwb.get_sheet(0)
    for i in range(len(data)):
        sh.write(i + 1, 10, data[i])
    wwb.save('data_filtered.xls')
