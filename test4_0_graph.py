import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time

start = time.process_time()
G = nx.Graph()
# df = pd.read_csv('社团划分.csv', encoding="utf-8")
# 该文件53985409行
reader = pd.read_csv('test4_0_gexf.csv', iterator=True, encoding="utf-8")
chunksize = 1000000
df_list = list()
start1 = time.process_time()
while True:
    try:
        df = reader.get_chunk(chunksize)
        df_list.append(df)
    except StopIteration:
        end1 = time.process_time()
        print('读取完文件', str(end1-start1))
        break
df = pd.concat(df_list)
G = nx.from_pandas_edgelist(df, '实体', '值', '属性')
end2 = time.process_time()
print('数据加载到G中', str(end2-end1))

cli = nx.find_cliques(G)
nodes_list = nx.algorithms.community.k_clique_communities(G, 2, cli)
end3 = time.process_time()
print('社团划分完成', str(end3-end2))

# np_list = np.array(nodes_list)
# np.savetxt('np_list.txt', np_list)
# output = open('np_list.txt', 'w+', encoding='utf-8')
# for i in range(len(nodes_list)):
#     for j in range(len(nodes_list[i])):
#         output.write(str(nodes_list[i][j]), ' ')
#     output.write('\n')

df = pd.DataFrame(nodes_list)
# header=None
df.to_csv('nodes_list.csv', encoding='utf-8', index=False, header=None)

end4 = time.process_time()
print('保存文件完成', str(end4-end3))

"""
{0: [0, '女装', '雁荡山', '灵峰'], 
 1: [1, '超线程', '英特尔'], 
 2: ['免费域名', 2, '域名'], 
 3: ['结构化查询语言', 3, '数据库'], 
 4: ['战术', 4, 'rush战术'], 
 5: [nan, '蕉心格', '美国[美利坚合众国]', 145, '倪虹洁', '武林外传[2006年章回体古装情景喜剧]', '广告', 'QQ', '加拿大[北美洲国家]', '...', '摘领格', '深圳', '房前屋后', '黄页[传统黄页]', 'QQ空间', '腾讯', '北美洲', '宁财神', '百慕大三角[魔鬼三角海域]', '腾讯网', '石家庄众美广告', '内附格', '祝无双[电视剧《武林外传》中的人物]', '马化腾'],
 ……}
"""
