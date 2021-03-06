#! /usr/bin/env python

def read_file(rd_file):
    with open(rd_file) as rf:
        lines = rf.readlines()
    imu = []
    enc = []
    ultra = []
    enc_err = 0
    imu_err = 0
    ult_err = 0

    for line in lines:
        if 'imu data' in line:
            if len(line.split(':')) != 3:
                imu_err += 1
                continue
            imu.append(line.split(':')[1].split(']')[0].strip())

        elif 'enc data' in line:
            if len(line.split(':')) != 2:
                enc_err += 1
                continue
            enc.append(line.split(':')[1].split(']')[0].strip())

        elif 'ultra data' in line:
            if len(line.split(':')) != 2:
                ult_err += 1
                continue
            ultra.append(line.split(':')[1].split(']')[0].strip())

        else:
            pass
    # print err count
    print('imu_err:' + str(imu_err) + ', enc_err: '+str(enc_err)+', ult_err: '+str(ult_err))

    with open('imu.txt', 'w') as wf:
        for i in imu:
            wf.write(i+'\n')
    with open('enc.txt', 'w') as wf:
        for i in enc:
            wf.write(i+'\n')
    with open('ult.txt', 'w') as wf:
        for i in ultra:
            wf.write(i+'\n')


if __name__ == '__main__':
    read_file('1.txt')
