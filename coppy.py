#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import xlrd
import xlrd
 
def strs(row):
    values = "";
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) 
    return values
 
# 打开文件
data = xlrd.open_workbook("002.xlsx")
sqlfile = open("1.txt", "a",encoding='utf-8') # 文件读写方式是追加
 
table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
print('表格一共有：%s行'%nrows)
print('表格一共有：%s列'%ncols)
print('表格的标题分别为：%s'%colnames)
for ronum in range(1, nrows):
        row = table.row_values(ronum)
        values = strs(row[0]) # 调用函数，将行数据拼接成字符串
        sqlfile.writelines(values + "\n") #将字符串写入新文件
sqlfile.close() # 关闭写入的文件件