# 将社团分割.csv的 实体（Id）和模块化类（modularity_class)两列提取出来 作为redis的第二个数据库
import redis
import csv
import pandas as pd

REDIS_HOST = 'localhost'
# 如果没密码的话，这里是空字符串
REDIS_PASS = '' 
# 端口号根据具体而定
REDIS_PORT = 6379

pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASS, port=REDIS_PORT, decode_responses=True)   
# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)

pipe=r.pipeline(transaction=True)

# pipe.multi()
# pipe.set('name', 'bar')
# pipe.set('role', 'foo')
# pipe.execute()

# 第一种打开方式，使用csv
# with open("社团划分.csv", 'rt', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     print (type(reader))
#     for row in reader:
#         Id = row['Id']
#         Modularity_class = row['modularity_class']
#         print (row)
#         r.set(Id, Modularity_class)

# 第二种打开方式，pandas
reader = pd.read_csv("社团划分.csv", encoding='utf-8', nrows=10)

for index, row in reader.iterrows():
    # print (index)
    # print (type(index))
    # print (row['Id'])
    # print (row)
    # print (type(row))

    Id = row['Id']
    Modularity_class = row['modularity_class']   
    r.set(Id, Modularity_class)


print (r.get('女装'))