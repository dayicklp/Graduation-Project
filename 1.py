# coding=utf-8  
import os  
import sys
import codecs
from tkinter import *
from tkinter import scrolledtext 
'''
@2016-01-07 By Eastmount
功能:合并实体名称和聚类结果 共类簇20类
输入:BH_EntityName.txt Cluster_Result.txt
输出:ZBH_Cluster_Merge.txt ZBH_Cluster_Result.txt
'''
 
source1 = open("1.txt",'r')
source2 = open("2.txt",'r',encoding='utf-8')
result1 = codecs.open("ZBH_Cluster_Result.txt", 'w', 'utf-8')
 
#########################################################################
#                        第一部分 合并实体名称和类簇
 
lable = []       #存储408个类标 20个类
content = []     #存储408个实体名称
name = source1.readline()
#总是多输出空格 故设置0 1使其输出一致
num = 1
while name!="":
    name = str(name.strip('\r\n'))
    if num == 1:
        res = source2.readline()
        res = res.strip('\r\n')
        
        value = res.split(' ')
        no = int(value[0]) - 1   #行号
        va = int(value[1])       #值
        lable.append(va)
        content.append(name)
        
        print(name, res)
        result1.write(name + ' ' + res + '\r\n')
   #     num = 0
   # elif num == 0:
  #      num = 1
    name = source1.readline()
    
else:
    print('OK')
    source1.close()
    source2.close()
    result1.close()
 
#测试输出 其中实体名称和类标一一对应
#i = 0
#while i < len(lable):
  #  print(content[i], (i+1), lable[i])
  #  i = i + 1
 
#########################################################################
#                      第二部分 合并类簇 类1 ..... 类2 .....
 
#定义定长50字符串数组 对应50个类簇
output = ['']*50
result2 = codecs.open("ZBH_Cluster_Merge.txt", 'w', 'utf-8')
 
#统计类标对应的实体名称
i = 0
while i < len(lable):
    output[lable[i]] += content[i] + '\r\n' 
    i = i + 1

i = 1
chu=''
#输出
while i < 50:
    print ('#######')
    result2.write('#######\r\n')
    chu+='#######\r\n'
    print ('Label: ' + str(i))
    result2.write('Label: ' + str(i) + '\r\n'+"\r\n")
    chu+='Label: ' + str(i) + '\r\n'+"\r\n"
    print (output[i])
    result2.write(output[i] + '\r\n')
    chu+=output[i] + '\r\n'
    i = i + 1
 
result2.close()

''''
max=[]
i=0
while i < 50:
    if len(output[i]) > len(max):
        max=output[i]
    i=i+1
print(max)
'''


root=Tk()
root.title("话题聚类结果")
S=Scrollbar(root)
T=Text(root,height=50,width=120,font =("宋体", 14,
"normal"))
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT,fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote=chu
T.insert(END,quote)
mainloop()









