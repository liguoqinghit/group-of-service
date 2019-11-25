import networkx as nx
import csv
import pandas as pd
import numpy as np
import sys
import redis
import time

reader = pd.read_csv(r'ownthink_v2.csv', iterator=True, encoding="utf-8-sig")
# reader = pd.read_csv(r'C:\work\graph_of_knowledge\data\ownthink_v2.csv', iterator=True, encoding="utf-8-sig")
chunksize = 100000

REDIS_HOST = '192.168.1.118'
# 如果没密码的话，这里是空字符串
# REDIS_PASS = ''
num_index = 100000
REDIS_PORT = 26379

# list_all3 把每次循环导出的list_all2整合到一起
list_all3 = []
i = 1
# 按块提取思知文件
start = time.process_time()
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
loop = True
while loop:
    try:
        start1 = time.process_time()
        data = reader.get_chunk(chunksize)

        # 去除有空数据
        data = data.dropna(axis=0)
        list_sismember = []

        # 第一次筛选出当前行实体不包含值且值不包含实体 存入list_all1
        list_all1 = []
        data = np.array(data)
        data = data.tolist()
        for row in data:
            if str(row[0]) in str(row[2]) or str(row[2]) in str(row[0]):
                continue
            else:
                pipe.sismember('entity', row[2])
                list_all1.append(row)
        list_sismember = pipe.execute()

        # 第二次筛选出返回结果为True的 存入list_all2
        list_all2 = []
        index = 0
        for sismember in list_sismember:
            if sismember:
                list_all2.append(list_all1[index])
            index += 1

        list_all3 = list_all3 + list_all2
        end1 = time.process_time()
        print("第%d次读取文件结束" % i)
        print(str(end1-start1))
        i += 1
    except StopIteration:
        loop = False
        print('Iteration is stopped')

pd_all2 = pd.DataFrame(list_all3, columns=['实体', '属性', '值'])

filename = 'test4_0_gexf.csv'
print('开始写入数据')
start4 = time.process_time()
pd_all2.to_csv(filename)
end4 = time.process_time()
print('写入数据结束')
print(str(end4-start4))


# G = nx.Graph()

# # 转换数据
# print('开始转换数据')
# start3 = time.process_time()
# # 此时只添加了含关系的结点
# G = nx.from_pandas_edgelist(pd_all2, '实体', '值', ['属性'])
# end3 = time.process_time()
# print('转换数据结束')
# print(str(end3-start3))

print('写入数据结束')
print(str(end4-start4))
#
pipe.close()
r.close()
print('complete------------------------------------------------------')
print('总计时'+str(end4-start))
