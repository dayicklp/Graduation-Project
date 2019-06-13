# -*- coding:utf-8 -*-  
import jieba

#导入自定义词典
jieba.load_userdict("dict_news.txt")
# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('stopwords.txt',encoding='utf-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "1.txt"
outfilename = "out.txt"
inputs = open(filename, 'rb')
outputs = open(outfilename, 'w',encoding='utf-8')

# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")