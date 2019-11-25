import redis
import pandas as pd
import numpy as np
import os

REDIS_HOST = 'localhost'
# 如果没密码的话，这里是空字符串
REDIS_PASS = '' 
# 端口号根据具体而定
# REDIS_PORT = 6379

# 修改数据库（实体名），模块化类的数据导入数据库1的value中，使数据库1存储（实体名和模块化类）
def modify_db_entity_class(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASS, port=REDIS_PORT, decode_responses=True)   
    r = redis.Redis(connection_pool=pool)

    for index, row in iterrows:
        r.hset('entity', row['Id'], row['modularity_class'])

# 创建数据库（存储实体名、属性和值）
def create_db_entity_attribute_value(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASS, port=REDIS_PORT, decode_responses=True)   
    r = redis.Redis(connection_pool=pool)

    for index, row in iterrows:
        r.hset(row['实体'], row['属性'], row['值'])
        
        # 测试用，只检测前面12行数据
        if index == 12:
            print (r.hgetall('词条'))
            break
# 创建数据库（模块化类和实体名）
def create_db_class_entity(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, password=REDIS_PASS, port=REDIS_PORT, decode_responses=True)   
    r = redis.Redis(connection_pool=pool)

    for index, row in iterrows:

        r.hset(row['modularity_class'], row['Id'], 1)
        
        # 测试用，只检测前面12行数据
        if index == 12:
            print (r.hgetall('0'))
            break


REDIS_PORT = 6379
print ('第一步，打开文件')
reader_class = pd.read_csv("社团划分.csv", encoding='utf-8', nrows=20)
print ('第二步，创建数据库_类_实体')
create_db_class_entity(REDIS_PORT, reader_class.iterrows())

print ('第一步，打开文件')
reader_entity = pd.read_csv("entity4.csv", encoding='utf-8', nrows=20)
print ('第二步，创建数据库实体_属性_值')
create_db_entity_attribute_value(6379, reader_entity.iterrows())