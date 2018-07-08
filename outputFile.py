#!/usr/bin/env python
#coding:utf8

#import os
#import sys

class OutputFile(object):
    """docstring for Hotel"""
    def __init__(self,fileName,text,mode='a'):
        self.fileName = fileName
        self.text = text
        self.mode = mode

    def output(self):
        #print(self.text)
        wFile = open(self.fileName,self.mode)        
        wFile.write(self.text)
        wFile.close()

if __name__ == '__main__':
    Myoutput = OutputFile('mytest','test content')
    Myoutput.output()












