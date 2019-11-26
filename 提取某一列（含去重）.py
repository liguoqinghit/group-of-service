import pandas as pd
import csv


def drop_duplicate_column(filename, dup_column, filename2):

    df = pd.read_csv(filename, encoding="utf-8")
    df.drop_duplicates(subset=[df.columns[dup_column]], keep='first', inplace=True)
    df = df[df.columns[dup_column]]
    df_list = df.values.tolist()
    with open(filename2, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for i in df_list:
            # i = list(i) 不可行 不知道为什么
            i = [i]
            writer.writerow(i)
    print("提取完毕")


filename = "食物.csv"
dup_column = 2
filename2 = "食物关系.csv"
# filename = "旅游.csv"
# dup_column = 2
# filename2 = "旅游关系.csv"
drop_duplicate_column(filename, dup_column, filename2)

