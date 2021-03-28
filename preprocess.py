import numpy as np

# A : 4; C : 2; G : 1; T : 0

fin = open('./dna.data', 'r')
fout_str = ""
# list2array = []
# DNA_pois_array = np.empty((2000, 60), dtype = int)
DNA_pois_array = np.empty([], dtype = int)
DNA_clas_array = np.empty([], dtype = int)

# 第一行单独处理先得一个array再append / 去掉第一个元素

for line in  fin.readlines():
    # line_no_space = str(line.split())
    # list2array.clear()
    for i in range(0, len(line) - 3, 6): # "\n"占1
        if line[i] == "1":
            fout_str += 'A'
            #list2array.append(1)
            DNA_pois_array = np.append(DNA_pois_array, [4])
        elif line[i + 2] == "1":
            fout_str += 'C'
            DNA_pois_array = np.append(DNA_pois_array, [2])
        elif line[i + 4] == "1":
            fout_str += 'G'
            DNA_pois_array = np.append(DNA_pois_array, [1])
        else:
            fout_str += 'T'
            DNA_pois_array = np.append(DNA_pois_array, [0])
            # fout_str.append("T")

    
    if line[-3] == "1":
        fout_str += " ei\n"
        DNA_clas_array = np.append(DNA_clas_array, [1])
    elif line[-3] == "2":
        fout_str += " ie\n"
        DNA_clas_array = np.append(DNA_clas_array, [2])
    else:
        fout_str += " n\n"
        DNA_clas_array = np.append(DNA_clas_array, [3])

# 用空数组接第一个元素不为空要删除
DNA_pois_array = np.delete(DNA_pois_array, 0)
DNA_clas_array = np.delete(DNA_clas_array, 0)
DNA_pois_array = np.reshape(DNA_pois_array, (2000, 60))
print(DNA_pois_array)
print(DNA_clas_array)
        
fout = open('./dna_data.pre', 'w')
fout.write(fout_str)

fin.close()
fout.close()




"""
fin = open('./dna.data', 'r')
fout_str = ""
for line in  fin.readlines():
    # line_no_space = str(line.split())
    for i in range(0, len(line) - 3, 6):
        if line[i] == "1":
            fout_str += 'A'
        elif line[i + 2] == "1":
            fout_str += 'C'
        elif line[i + 4] == "1":
            fout_str += 'G'
        else:
            fout_str += 'T'
            # fout_str.append("T")

    
    if line[-3] == "1":
        fout_str += " ei\n"
    elif line[-3] == "2":
        fout_str += " ie\n"
    else:
        fout_str += " n\n"
        
fout = open('./dna_data.pre', 'w')
fout.write(fout_str)

fin.close()
fout.close()
"""

"""
fin = open('./dna.data', 'r')
line = fin.readline()
fout_str = ""
for i in range(0, len(line) - 3, 6):
    if line[i] == "1":
        fout_str += 'A'
    elif line[i + 2] == "1":
        fout_str += 'C'
    elif line[i + 4] == "1":
        fout_str += 'G'
    else:
        fout_str += 'T'
print(fout_str)
print(line[-1])
print(line[-2])
print(line[-3])
"""