# group-of-service
test4_0_1.py和test4_0_2.py 仅创建一个数据库(好像还有问题，未改)
test4_0_总.py 试验成功，在本地创建两个数据库
test4_1.py 总体框架(包含创建三个数据库和对村淘实体的有关搜索，部分测试已经可以，还需要修改)
dic_to_csv.py 测试字典转化为csv文件
test4_0_gexf.py 处理思知的数据生成csv文件(因为gexf的文件过大，gephi不能处理)
test4_0_graph.py 根据数据生成G，使用networkx进行社团划分，预计导出和gephi一样的数据(实体+modularity_class)

# 读取文件行数，大约8秒/G
count = 0
for index, line in enumerate(open(filepath, 'r')):
    count += 1
print(count)
