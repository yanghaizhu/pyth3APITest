#!/usr/bin/env python
#coding:utf8

import outputFile
from enumRelation import enumRelation

class Relation(object):
    """docstring for Hotel"""
    def __init__(self,first,relation,second):
        self.first = first
        self.second = second
        self.enum = relation
        self.start = '{['
        self.end = ']}'
        self.fileRelation = 'test/relation.txt'
        if(relation ==enumRelation.isPartOf):
            self.filename = 'test/isPartOf.txt'
            self.lianjie = '#isPartOf#'
        if(relation ==enumRelation.isSameAs):
            self.filename = 'test/isSameAs.txt'
            self.lianjie = '#isSameAs#'
        if(relation ==enumRelation.isRefine):
            self.filename = 'test/isRefine.txt'
            self.lianjie = '#isRefine#'
        if(relation ==enumRelation.isProduceOf):
            self.filename = 'test/isProduceOf.txt'
            self.lianjie = '#isProduceOf#'
        if(relation ==enumRelation.isConsumerOf):
            self.filename = 'test/isConsumerOf.txt'
            self.lianjie = '#isConsumerOf#'
        if(relation ==enumRelation.isMaterialOf):
            self.filename = 'test/isMaterialOf.txt'
            self.lianjie = '#isMaterialOf#'
        if(relation ==enumRelation.isDescriptionOf):
            self.filename = 'test/isDescriptionOf.txt'
            self.lianjie = '#isDescriptionOf#'
        if(relation ==enumRelation.isPropertyOf):
            self.filename = 'test/isPropertyOf.txt'
            self.lianjie = '#isPropertyOf#'

    def outputRelation(self,):
        guanxiText = self.start+self.first+self.lianjie+self.second+self.end        
        fileout = outputFile.OutputFile(self.fileRelation,guanxiText)
        fileout.output();
        text = '{'+self.first+'#'+self.second+'}'
        fileout = outputFile.OutputFile(self.filename,text)
        fileout.output();


if __name__ == '__main__':
    Relation('part',enumRelation.isPartOf,'whole').outputRelation()
    Relation('name1',enumRelation.isSameAs,'name2').outputRelation()
    Relation('fineClass',enumRelation.isRefine,'class').outputRelation()













