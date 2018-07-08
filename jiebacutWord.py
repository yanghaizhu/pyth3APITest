#!/usr/bin/env python
#coding:utf8

import jieba



class jiebaCutWords(object):
    """docstring for Hotel"""
    def __init__(self,sentence):
        self.sentence = sentence        

    def cutWords(self,):
        seg_list = jieba.cut(self.sentence)
        #print("/".join(seg_list))
        return seg_list


if __name__ == '__main__':
    seg_list = jiebaCutWords("他去过清华大学和北京大学").cutWords()
    for seg in seg_list:
        print(seg)
    







