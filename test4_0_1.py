# 将entity4.csv的 实体、属性和值三列提取出来 作为redis的第一个数据库（关系这个还没加入到数据库，为方便处理，暂不加入）
import redis
import pandas as pd
import numpy

REDIS_HOST = 'localhost'
# 如果没密码的话，这里是空字符串
REDIS_PASS = '' 
# 端口号根据具体而定
REDIS_PORT = 6379

# pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASS, port=REDIS_PORT, decode_responses=True)   
# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# r = redis.Redis(connection_pool=pool)

# pipe=r.pipeline(transaction=True)

# pipe.multi()
# pipe.set('name', 'bar')
# pipe.set('role', 'foo')
# pipe.execute()

reader = pd.read_csv("entity4.csv", encoding='utf-8', nrows=20)


# hmset(name, mapping)
# 以实体为name，以属性和值建立mapping（类似dictionary）
# 需要判断当前实体与上一个实体是否为同一实体，若是将后面的属性和值存储到dic中，否则。。。
dic = {}
last_entity = ''
for index, row in reader.iterrows():
    # print (row.tolist())
    # print (type(row))
    # print (row.values)
    # print (type(row.values))
    # print (row.values[1])
    # print (row.index)
    # print (type(row.index))

    if index == 0:
        dic[row['属性']] = row['值']    
    elif last_entity == row['实体']:
        dic[row['属性']] = row['值']
    else:
        print (last_entity)
        print (dic)
        # 传输到redis
        # hmset (last_entity, dic)
        dic = {}
    last_entity = row['实体']

    # 测试用，只检测前面12行数据
    # if index == 12:
    #     break
# print ('over')
# print (dic)

# print (r.get('女装'))