import numpy as np
import pandas as pd
import time

# start = time.process_time()
# np_list = np.loadtxt('np_list.txt')
# nodes_list = np_list.tolist()
# modularity_class = 0
# all_list = list()
# for nodes in nodes_list:
#     for node in nodes:
#         class_node = [modularity_class, node]
#         all_list.append(class_node)
#     modularity_class += 1
#
# df = pd.DataFrame(all_list, columns=['modularity_class', 'entity'])
# df.to_csv('graph.csv', encoding='utf-8', index=False)
# end = time.process_time()
# print('生成类_实体csv文件', str(end-start))

reader = pd.read_csv('nodes_list.csv', iterator=True, encoding='utf-8')


