import pandas as pd
import csv


inp = {'x1': {'c4': 10, 'c2': 100}, 'x2': {'c6': 11, 'c1': 110}, 'x3': {'c1': 12, 'c2': 120}}
all_list = list()
column_list = ['实体', '属性', '值']
# 遍历字典
for k, v in inp.items():
    # print (k)
    for vk, vv in v.items():
        all_list.append([k, vk, vv])
    #     print (vk)
    #     print (vv)
    #     print ('2---')
    # print ('1----')
print(all_list)

df = pd.DataFrame(data=all_list, columns=column_list)
print(df)

df.to_csv('try.csv', encoding='utf-8', index=False)

i = 1
str1 = "abc.csv"
print(str1)
str1_list = list(str1)
pos = str1.index('.')
str1_list.insert(pos, str(i))
str1 = ''.join(str1_list)
print(str1)

