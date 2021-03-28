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