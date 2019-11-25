import igraph as ig
from igraph import *
import time

start = time.process_time()
num_vertex = 100000000
# num_vertex = 1000
num_edge = 50000000
# num_edge = 500
num_edge_ran = 50000
# num_edge_ran = 5
g = Graph()

# 加点
g.add_vertices(num_vertex)
# for i in range(0, num_edge):
#     g.add_edge(i, i+1)
#     if i % (num_edge/num_edge_ran) == 0:
#         i += 2
# 加边
edge_list = []
for i in range(0, num_edge):
    edge_list.append([i, i+1])
    if i % (num_edge/num_edge_ran) == 0:
        print('跳过一次，%s' % i)
        i += 2
g.add_edges(edge_list)
end1 = time.process_time()
print(end1-start)
print('创建完图，并开始社团划分')

g_list = g.community_infomap()
end2 = time.process_time()
print(end2-end1)
print('社团划分完毕，并开始保存文件')
index = 0
for community in g_list:
    with open('./community_infomap/list%s.txt' % index, 'w') as f:
        for entity in community:
            f.write(str(entity))
    index += 1
    if i % (num_edge_ran*100):
        print('第%s写入文件' % index)

end3 = time.process_time()
print(end3-end2)
print('写入文件完毕')


