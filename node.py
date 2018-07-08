#!/usr/bin/env python
#coding:utf8

#import os
#import sys

class node():
    def __init__(self,mean=0,cov=0):
        self.mean=mean
        self.cov=cov

    def speak(self):
        print(self.mean)
        print(self.cov)
        
if __name__ == '__main__':
    myNode = node(0,0)
    myNode.speak()

