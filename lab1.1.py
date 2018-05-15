import numpy as np
import matplotlib.pyplot as plt
file = open('magic04.txt')
Data = [    [float(i) for i in a.split(',')[:-1]] for a in file.readlines()]
matrix = np.array(Data)#矩阵
mean = np.mean(matrix, axis=0)
print(mean)  #Q1

mean1=np.transpose(mean)
n = matrix.shape[0]#行
temp=[1 for i in range(n)]
tm=np.matrix(temp)
tm = np.transpose(tm)
temp1=tm*mean1
z=matrix-temp1  #中心矩阵
zt=np.transpose(z)
inner=zt*z/3
print(inner)  #Q2

Sum=0
zp=[0 for i in range(n)]
for i in range(n):
  zp[i]=np.transpose(z[i])
  temp2=zp[i]*z[i]
  Sum+=temp2
Sum=Sum/3
print(Sum)  #Q3

lie1 = matrix[:, 0]
lie2 = matrix[:, 1]
cos = np.dot(lie1, lie2)/(np.dot(lie1, lie1) *np.dot(lie2, lie2))
print(cos)
plt.scatter(lie1,lie2)
plt.show()   #Q4


mt=np.transpose(matrix)
v=[0 for i in range(10)]
for i in range(10):
  narray=np.array(mt[i])
  temp1=narray.sum()
  narray2=narray*narray
  temp2=narray2.sum()
  avr=temp1/n
  v[i]=temp2/n-avr**2
print(v)                      #Q6
