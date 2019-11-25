import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time
import igraph as ig

start = time.process_time()
G = nx.Graph()
# 该文件53985409行
# reader = pd.read_csv('test4_0_gexf.csv', iterator=True, encoding="utf-8")
reader = pd.read_csv('社团划分.csv', iterator=True, encoding="utf-8")
# reader = pd.read_csv('entity4.csv', iterator=True, encoding="utf-8")
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
# G = nx.from_pandas_edgelist(df, '实体', '值', '属性')
G = nx.from_pandas_edgelist(df, 'Id', 'modularity_class')
end2 = time.process_time()
print('数据加载到G中', str(end2-end1))
# end3 = time.process_time()
# nx.write_pajek(G, 'networkx_graph.net', encoding='utf-8')
# nx.write_graphml(G, 'networkx_graph.graphhml', encoding='utf-8')
# end4 = time.process_time()
# print('保存文件完成', str(end4-end3))
# print('总时间', end4-start)

# IG = ig.Graph()
# IG.add_vertices(G.number_of_nodes())
# 添加attribute
# IG[0] = '女装'
# print(IG[0])

# print(IG.es.get_attribute_values('女装'))
# print(IG.__getattribute__(0))



