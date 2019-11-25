import redis
import pandas as pd
import numpy as np
import os
import csv

REDIS_HOST = '192.168.1.118'
num_index = 100000


# 创建数据库（实体名和模块化类 1：1）
def create_db_entity_class(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    index = 0
    for row in iterrows:
        pipe.hset('entity_class', row['Id'], row['modularity_class'])
        # 提交数据
        if index % num_index == 0:
            print('第%s次提交' % str(int(index / num_index + 1)))
            pipe.execute()
        index += 1
    pipe.execute()
    pipe.close()
    r.close()
    print('创建数据库（实体名和模块化类）')


# 创建数据库（存储实体名、属性和值）
def create_db_entity_attribute_value(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    index = 0
    for row in iterrows:
        pipe.hset(row['实体'], row['属性'], row['值'])
        # 提交数据
        if index % num_index == 0:
            print('第%s次提交' % str(int(index / num_index + 1)))
            pipe.execute()
        index += 1
    pipe.execute()
    print('创建数据库（存储实体名、属性和值）')
    pipe.close()
    r.close()


# 创建数据库（模块化类和实体名 1：n）
def create_db_class_entity(REDIS_PORT, iterrows):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    index = 0
    for row in iterrows:
        pipe.hset(row['modularity_class'], row['Id'], 1)
        # 提交数据
        if index % num_index == 0:
            print('第%s次提交' % str(int(index / num_index + 1)))
            pipe.execute()
        index += 1
    pipe.execute()
    print('创建数据库（模块化类和实体名）')
    pipe.close()
    r.close()


# 通过村淘实体找到所需三元组
# 第一步，找到包含村淘实体的模块化类
def entity_to_tuple_class(REDIS_PORT, entity_list):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    # class_set 存储导出模块化类
    class_set = set()

    # pipe 传递 是否存在实体
    index = 0
    list_hexists = []
    for entity in entity_list:
        index += 1
        pipe.hexists('entity_class', entity)
        if index % num_index == 0:
            list_hexists.append(pipe.execute())
    list_hexists.append(pipe.execute())

    # pipe 传递 实体的模块化类
    index = 0
    list_hget = []
    for hexists1 in list_hexists:
        for hexists2 in hexists1:
            if hexists2:
                print(hexists2)
                print(entity_list[index])
                pipe.hget('entity_class', entity_list[index])
                if index % num_index == 0:
                    list_hget.append(pipe.execute())
            index += 1
    list_hget.append(pipe.execute())

    # 把实体的模块化类存放在set里面
    for hget1 in list_hget:
        for hget2 in hget1:
            class_set.add(hget2)

    print('找到包含村淘实体的模块化类')
    print(class_set)
    pipe.close()
    r.close()
    return class_set


# 第二步，根据上面导出的模块化类找出所对应的所有实体
def entity_to_tuple_entity(REDIS_PORT, class_set):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    # eneity_list 存储导出的所有实体
    entity_list = list()

    # pipe 传递 模块化类对应的所有实体
    index = 0
    hkeys_list = []
    for modularity_class in class_set:
        index += 1
        pipe.hkeys(modularity_class)
        if index % num_index == 0:
            hkeys_list.append(pipe.execute())
    hkeys_list.append(pipe.execute())

    # 把模块化类对应的所有实体存到entity_list
    for hkeys1 in hkeys_list:
        for hkeys2 in hkeys1:
            entity_list.append(hkeys2)

    print('找到包含村淘实体的模块化类')
    print(entity_list)
    pipe.close()
    r.close()
    return entity_list


# 第三步，根据上面导出的实体导出对应实体的所有信息
def entity_to_tuple_all(REDIS_PORT, entity_list):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline(transaction=True)
    # all_dic 存储所有实体信息 {实体: {属性, 值}}
    all_dic = dict()

    # pipe 传递 实体对应的所有信息
    index = 0
    hgetall_list = []
    all_entity = []
    for entity_list_class in entity_list:
        for entity in entity_list_class:
            all_entity.append(entity)
            index += 1
            pipe.hgetall(entity)
            if index % num_index == 0:
                hgetall_list.append(pipe.execute())
    hgetall_list.append(pipe.execute())

    # 将实体对应的所有信息存到all_dic
    index = 0
    for hgetall1 in hgetall_list:
        for hgetall2 in hgetall1:
            all_dic[all_entity[index]] = hgetall2
            index += 1

    print('根据上面导出的实体导出对应实体的所有信息')
    print(all_dic)
    pipe.close()
    r.close()
    return all_dic


# 第四步，把字典转化为三元组（存入csv文件）
def entity_to_tuple_tocsv(all_dic):
    all_list = list()
    column_list = ['实体', '属性', '值']

    for entity, attribute_value in all_dic.items():
        for attribute, value in attribute_value.items():
            all_list.append([entity, attribute, value])

    df = pd.DataFrame(data=all_list, columns=column_list)
    df.to_csv('information.csv', encoding='utf-8', index=False)
    print('已生成information.csv文件')


# 主函数部分
# 定义三个数据库的端口号
REDIS_PORT_entity = 26379
REDIS_PORT_class = 26380
REDIS_PORT_all = 26381

print('1，打开文件 社团划分.csv')
reader_class = pd.read_csv("社团划分.csv", encoding='utf-8')
data_class = np.array(reader_class)
data_class = data_class.tolist()
print('2，创建数据库_类_实体')
create_db_class_entity(REDIS_PORT_class, data_class)

print('3，修改数据库_实体为数据库_实体_类')
create_db_entity_class(REDIS_PORT_entity, data_class)

print('4，打开文件 entity4.csv')
reader_entity = pd.read_csv("entity4.csv", encoding='utf-8')
data_entity = np.array(reader_entity)
data_entity = data_entity.tolist()
print('5，创建数据库实体_属性_值')
create_db_entity_attribute_value(REDIS_PORT_all, data_entity)

# 村淘实体
entity = ['女装', '男装', '运动', '手表眼镜', '鞋包饰品',
          '粮油美食', '日化洗护', '母婴玩具', '办公影音',
          '家用电器', '手机通信', '家装建材', '家具家私',
          '种子', '肥料', '饲料', '机具', '农膜', '农药',
          '新车', '摩托', '电动', '汽车精品', '汽摩配件']
print('6，找到包含村淘实体的模块化类')
class_set = entity_to_tuple_class(REDIS_PORT_entity, entity)
print('7，根据上面导出的模块化类找出所对应的所有实体')
entity_list = entity_to_tuple_entity(REDIS_PORT_class, class_set)
print('8，根据上面导出的实体导出对应实体的所有信息')
all_dic = entity_to_tuple_all(REDIS_PORT_all, entity_list)
print('9，把字典转化为三元组（存入csv文件）')
entity_to_tuple_tocsv(all_dic)
print('10，完成！！')
