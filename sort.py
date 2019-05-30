import numpy as np

a = [[[6.8,2.1,8.2,4.2],'1'], #[[3.1, 2.3, 5.3, 4],'2'],[[1,2,3,4],'3']]
     [[3.3, 4.0,5.5,6.3],'4'], # [[1.2,4.1,3.2,6.7],'5'],
     [[1.1,8.3,2.9,10.1],'6']]

clusters = []
cluster = []
cluster.append(a[0])
for aa in a[1:]:
    if cluster[0][0][3] - cluster[0][0][1] > 2 *(aa[0][1] -cluster[0][0][1]):
        cluster.append(aa)
    else:
        clusters.append(cluster)
        cluster=[]
        cluster.append(aa)

clusters.append(cluster)
for i, cl in enumerate(clusters):
    clusters[i] = sorted(cl)

for cluster in clusters:
    print cluster

detector0 = []
for i, de in enumerate(clusters):
    detector0.append(str(i))
    detector0.extend(de)
# print detector0
