import pandas as pd
import csv


def count_relaton(filename, col, filename2):
    with open(filename2, 'r', encoding='utf-8') as file:
        relation_list = file.read().splitlines()
    dic = dict()
    for i in relation_list:
        dic[i] = 0
    df = pd.read_csv(filename, encoding="utf-8")
    df_list = df.values.tolist()
    for i in df_list:
        if i[col] in relation_list:
            dic[i[col]] += 1

    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    with open(filename2, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dic.items():
            writer.writerow([key, value])
    print("重新写入完毕")


# filename = '食物.csv'
# col = 2
# filename2 = '食物关系.csv'
filename = '旅游.csv'
col = 2
filename2 = '旅游关系.csv'
count_relaton(filename, col, filename2)

