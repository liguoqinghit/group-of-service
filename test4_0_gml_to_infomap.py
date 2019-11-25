import networkx as nx
import igraph as ig
from igraph import *
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib


# G = nx.read_graphml('networkx_graph.graphhml')
# 不知道为啥读的很慢CPU已经跑满
# nx.draw(G, with_labels=True)
# matplotlib.rcParams['font.sans-serif'] = ['SimHel']
# matplotlib.rcParams['font.family'] = 'sans-serif'
# plt.show()

# start = time.process_time()
# print(start)
# IG = load('networkx_graph.graphhml')
# IG = Graph.Read_GraphML('networkx_graph.graphhml')
# Graph.Read_GraphML()
# IG = ig.Graph.Read_Pajek('networkx_graph.net')
# print(type(IG))
# end1 = time.process_time()
# print('读取文件完毕', end1-start)
# g_list = IG.community_infomap()
# end2 = time.process_time()
# print(g_list)
# print('社团划分完毕', end2-end1)

IG = Graph()
# IG.add_vertex('女装', [1, 2])  # 不可行的
IG.add_vertex([1, 2])  # 可行的
# IG.add_vertex(0, [[1, 2]])  # 不可行的
# IG.add_vertex
IG.vs['女装'] = 0

print(IG)
# summary(IG)  # 不包含边，比print简单

# print(IG.vs[0])  # 输出了第一个点的物理地址、ID 以及 属性和值的集合
# print(IG.vertex_attributes())  # 输出IG的attribute
# print(IG['女装'])  # 不可行的
# print(IG['name'])  # 不可行的
# print(IG[name])  # 不可行的
# print(IG.vertex[1])  # 不可行的
# print(IG.es['name'])  # 可行的, 但是这是边属性，还没添加边
# print(IG.vs['name'])  # 输出[[1, 2]], 点属性
# g = Graph.Tree(127, 2)  # 生成树 127个节点，子节点2个
# IG.get_edgelist()[0: 10]  # 得到边表的前十个
# IG.get_eid(2, 3)  # 根据两节点ID得到对应边的ID
# IG.get_eids([(2, 3), (1, 3)])  # 得到一组边ID
# print(IG.vertex_attributes())  # 输出IG的点属性
# g = Graph.GRG(100, 0.2)  #生成随机图 100个节点 radius 半径范围0.2
# IG.Graph.GRG 也可以
# IG.isomorphic(g)  # 判断IG和g是否同构，不适合大的图，需要消耗太多时间，简单的图只需要通过两个图的度分布即可
# 保存文件的时候 属性只有是字符和数字的才能会被保存
# 如果你正在寻找一个保存其他属性类型的方式，请参见标准python库中pickle模块

# 定义一个图
g = Graph([(0, 1), (0, 2), (2, 3)])
# 定义顶点的三个属性 name age gender
g.vs['name'] = ['a', 'b', 'c', 'd']
g.vs['age'] = [11, 22, 33, 44, 55]
g.vs['gender'] = ['f', 'm', 'm', 'f']
# 定义边的属性 正式友谊or非
g.es['is_formal'] = [True, True, False]


# 生成1亿个节点的尝试能否运行
# 5000W个边
























