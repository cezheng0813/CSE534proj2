import pandas as pd
import numpy as np
file='defense-605.csv'
data = pd.read_csv(file, header=None, sep=',', skiprows=1)
lines=[]
f = open("defense_1_ok.txt")
line = f.readline()
while line:
    line = f.readline()
    line = line.strip('\n')
    lines.append(line)
# print(lines[0])
data = data.drop([0], axis=1)
data = data.values
a=data[0][0][62:]
list1=[]
for i in range(0,100,1):
    list1.append(data[i][0][62:-4])
# print(list1)
count=0
for i in range(0,len(lines),1):
    for j in range(0,100,1):
        if str(list1[j])==str(lines[i]):
            count+=1
        else:
            continue
print(count/100)














