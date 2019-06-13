# coding=utf-8  
""" 
Created on 2016-01-06 @author: Eastmount  
"""  
  
import time          
import re          
import os  
import sys
import codecs
import shutil
import numpy as np
from sklearn.manifold import TSNE
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
import matplotlib.pyplot as plt
 
if __name__ == "__main__":
    
    #########################################################################
    #                           第一步 计算TFIDF
    
    #文档预料 空格连接
    corpus = []
    
    #读取预料 一行预料为一个文档
    for line in open('out.txt', 'r',encoding='utf-8').readlines():
        #print(line)
        corpus.append(line.strip())
  

    #将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer() 
    #该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer() 
    #第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    #获取词袋模型中的所有词语  
    word = vectorizer.get_feature_names() 
    #将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

 
    #打印特征向量文本内容
   #print('Features length: ' + str(len(word)))
    resName = "BHTfidf_Result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
   # for j in range(len(word)):
     #   result.write(word[j] + ' ')
    #result.write('\r\n\r\n')
 
    #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
    for i in range(len(weight)):
       # print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------"  )
        for j in range(len(word)):
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')
    #print(weight)
    result.close()
 
    ########################################################################
    #                               第二步 聚类Kmeans
 
    print('Start Kmeans:')
    from sklearn.cluster import KMeans
    clf = KMeans(n_clusters=50,verbose=False)
    s = clf.fit(weight)
    print(s)
    #返回各自文本的所被分配到的类索引
    result = clf.fit_predict(weight)

    print("Predicting result: ", result)
    #50个中心点
    print(clf.cluster_centers_)
    #每个样本所属的簇
    print(clf.labels_)
    i = 1
    while i <= len(clf.labels_):
        print(i, clf.labels_[i-1])
        i = i + 1
   
    # 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
    # k-means的超参数n_clusters可以通过该值来评估
    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    print(clf.inertia_)



'''
    6、可视化
'''

# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components=2)
decomposition_data = tsne.fit_transform(weight)

x = []
y = []

for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()
plt.scatter(x, y,c=clf.labels_,s=25,alpha=0.4,marker='o')
#设置图标  
plt.legend()  
plt.xticks(())
plt.yticks(())
plt.savefig('./sample.png', aspect='equal')
plt.show()

'''
plt.figure(figsize=(9,6))
n=1000
#rand 均匀分布和 randn高斯分布
x=np.random.randn(1,n)
y=np.random.randn(1,n)
T=np.arctan2(x,y)
plt.scatter(x,y,c=T,s=25,alpha=0.4,marker='o')
#T:散点的颜色
#s：散点的大小
#alpha:是透明程度
plt.show()
'''