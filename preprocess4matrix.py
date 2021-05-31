import numpy as np

# A : 4; C : 2; G : 1; T : 0

fin = open('./dna.data', 'r')
DNA_pois_class_array = np.empty([], dtype = int)
# DNA_clas_array = np.empty([], dtype = int)

# 第一行单独处理先得一个array再append / 去掉第一个元素

for line in  fin.readlines():
    for i in range(0, len(line) - 3, 6): # "\n"占1
        if line[i] == "1":
            #fout_str += 'A'
            DNA_pois_class_array = np.append(DNA_pois_class_array, [4])
        elif line[i + 2] == "1":
            #fout_str += 'C'
            DNA_pois_class_array = np.append(DNA_pois_class_array, [2])
        elif line[i + 4] == "1":
            #fout_str += 'G'
            DNA_pois_class_array = np.append(DNA_pois_class_array, [1])
        else:
            #fout_str += 'T'
            DNA_pois_class_array = np.append(DNA_pois_class_array, [0])
            # fout_str.append("T")
  
    if line[-3] == "1":
        #fout_str += " ei\n"
        DNA_pois_class_array = np.append(DNA_pois_class_array, [1])
    elif line[-3] == "2":
        #fout_str += " ie\n"
        DNA_pois_class_array = np.append(DNA_pois_class_array, [2])
    else:
        #fout_str += " n\n"
        DNA_pois_class_array = np.append(DNA_pois_class_array, [3])

# 用空数组接第一个元素不为空要删除
DNA_pois_class_array = np.delete(DNA_pois_class_array, 0)
# DNA_clas_array = np.delete(DNA_clas_array, 0)
DNA_pois_class_array = np.reshape(DNA_pois_class_array, (2000, 61))
# DNA的位置信息与分类信息放在同一个array表示, array的最后一列表示类别
print(DNA_pois_class_array)
# print(DNA_clas_array)

fin.close()

