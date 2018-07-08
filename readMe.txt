enumRelation.py 枚举各种关系
outputFile.py 输入到文件，默认追加方式
outputRelation.py  将两者之间的关系写入文件
jiebaCutWords.py 断句分词

todo:
seqWords.py 词语关联度统计
wordFreqUpdate.py 词频统计
checkRelation.py 确定两者是那种关系






seg_list = jieba.cut("我去过清华大学和北京大学。")
print("全模式: " + "/ ".join(seg_list))

# 全模式

seg_list = jieba.cut("我去过清华大学和北京大学。", cut_all=True)
print("全模式: " + "/ ".join(seg_list))


# 搜索引擎模式

seg_list = jieba.cut_for_search("我去过清华大学和北京大学。")
print("搜索引擎模式: " + "/ ".join(seg_list))


# 精确模式/全模式下-新词发现 “杭研”没有在词典中，也被HMM模型 Viterbi算法识别出来

seg_list = jieba.cut("我去过清华大学和北京大学。",HMM=True)
print("精确模式/全模式-新词发现: " + "/ ".join(seg_list))


# 搜索引擎模式下-新词发现 “杭研”没有在词典中，也被HMM模型 Viterbi算法识别出来

seg_list = jieba.cut_for_search("我去过清华大学和北京大学。",HMM=True)
print("搜索引擎模式-新词发现: " + "/ ".join(seg_list))
