from os import lseek
import numpy as np
import math
x = np.empty((2, 3))
b = [1, 1, 1]
print(np.append(x, [b], axis = 0))
c = np.array([], dtype=int)
print(c)
d = np.append(c, b)

print(np.append(d, [2], axis = 0))
d = np.append(d, [3])
print(np.reshape(d, (2, 2)))
print(d)
print(np.delete(d, 3))

#print(np.append(c, [b], axis = 0))
a = "ACTGTGCA"
print(a)
print(list(a))
print(-(2+3))
print(math.log2(4))
f = np.reshape(d, (2, 2))
e = []
e.append(f[1])
print(e)
e.append(f[0])
print(e)
print(e[1])
g = np.array(e)
print(g)
"""
fin = open('./dna_data.pre', 'r')
line = fin.readline()
print(line)
# 接着读的
lines = fin.readlines()
print(lines)
"""

for i in [0,1,2,8]:
    print(i)

from collections import  Counter
data = np.array([1.1,2,3,4,4,5])
print(data)
lista = []
lista.append(data)
arrayE = np.array(lista)
print("hh")
print(lista)
lista.append(data)

print(arrayE)
print(lista)
print("hhh")
arrayb = np.array(lista)
print(arrayb[0][1])
print(np.delete(arrayb[0], 1))
print(arrayb[:,-1])
arrayc = arrayb[:,-1]
print(arrayc.shape[0])

print(Counter(data)[1.1])  # {label:sum(label)}
 
#简单方法
sum(data==4)
print(sum(data))

listha = [1,2,3]
print(listha)
del[listha[1]]
print(listha)

print(arrayb)
arrayb_true = (arrayb[:1] == 2.0)
print(arrayb_true)
print(type(arrayb_true))

listg = list(range(5))
print(listg)

print(arrayb[0, -1])