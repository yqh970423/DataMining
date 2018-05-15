import numpy as np
file = open("iris.txt")
Data = [    [float(i) for i in a.split(',')[:-1]] for a in file.readlines()]
matrix = np.array(Data)#矩阵
n = matrix.shape[0]#行
d = matrix.shape[1]#列

D= [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        D[i][j]=(np.dot(Data[i],Data[j]))**2
print(D)   #Q1