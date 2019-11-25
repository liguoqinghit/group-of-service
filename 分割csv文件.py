import pandas as pd
import time


def divide_csv(filename, chunk_size, num, filename2):
    """
    分割csv文件,将filename按chunk_size分割，提取num份，保存到filename2

    :param filename:
    :param chunk_size:
    :param num:
    :param filename2:
    :return:
    """
    reader = pd.read_csv(filename, iterator=True, encoding="utf-8")
    i = 0
    if num == 1:
        while i < num:
            df = reader.get_chunk(chunk_size)
            df.to_csv(filename2, encoding="utf-8")
            i += 1
        print("读取完文件")
    else:
        while i < num:
            try:
                df = reader.get_chunk(chunk_size)
                a = filename2
                a_list = list(a)
                pos = a_list.index('.')
                a_list.insert(pos, str(i))
                a = ''.join(a_list)
                df.to_csv(a, encoding="utf-8")
                i += 1
            except StopIteration:
                print("读取完文件")


filename = 'test4_0_gexf.csv'
chunk_size = 1_000_000
num = 1
filename2 = 'csv_100W.csv'

divide_csv(filename, chunk_size, num, filename2)

