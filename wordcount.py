#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import jieba
from collections import Counter
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import jieba.analyse
from pyquery import PyQuery
import xlwt #写入Excel表的库
from os import listdir



santi_text = open('1.txt', 'r').read() #读取本地文档

#jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数 


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist('./stopwords.txt')  # 这里加载停用词的路径
    santi_words =[x for x in sentence if len(x) >1 and x not in stopwords]

    return santi_words

def main():
    words = jieba.cut(PyQuery(santi_text).text()) #去除HTML标签
    word_list = movestopwords(words) # 去除停用词
    words_split = " ".join(word_list) #列表解析为字符串

    print('以下是tf-tdf算法-------------------------------------------------')
    keywords_tf = jieba.analyse.extract_tags(words_split, topK=60, withWeight=True,allowPOS=('ns', 'n', 'vn', 'v')) # tf-tdf算法
    for item in keywords_tf:
        print(item[0],item[1])
    with open("path.txt",'wt', encoding='utf-8') as f:
        for item in keywords_tf:
           print(item[0],item[1],file=f)
    with open("word.txt",'wt', encoding='utf-8') as f:
        for item in keywords_tf:
           print(item[0],file=f)
    print('以下是纯词频统计-------------------------------------------------')
    mycount = Counter(word_list) # 统计词频
    for key, val in mycount.most_common(100):  # 有序（返回前10个）
        print(key, val)
    '''
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
    tfidf=transformer.fit_transform(vectorizer.fit_transform(word_list))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重 
    word=vectorizer.get_feature_names()#获取词袋模型中的所有
    print(weight)
    
    mykms=KMeans(n_clusters=10)
    y=mykms.fit_predict(weight)
    for i in range(0,10):
        label_i=[]
        for j in range(0,len(y)):
            if y[j]==i:
                label_i.append(word[j])
        print('label_'+str(i)+':'+str(label_i))
    '''
    wc = WordCloud(
        width=800,
        height=600,
        background_color="white",  # 设置背景颜色
        max_words=50,  # 词的最大数（默认为200）
        max_font_size=400,  # 最大字体尺寸
        min_font_size=10,  # 最小字体尺寸（默认为4）
        random_state=70,  # 设置有多少种随机生成状态，即有多少种配色方案
        mask=imread("./1.png"),  # 读取遮罩图片！！
        font_path='c:\\windows\\Fonts\\STZHONGS.TTF'
    )


    my_wordcloud = wc.generate(words_split) #按词频生成词云
    plt.imshow(my_wordcloud) #展示词云
    plt.axis("off") #去除横纵轴
    plt.show()
    wc.to_file('zzz.png') # 保存图片文件

if __name__ == '__main__':
    main()

    


    
