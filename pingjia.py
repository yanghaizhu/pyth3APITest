from node import *
import math
class pingjia(object):
    def __init__(self,sourceNode,destiNode,value=0):
        self.value=value
        self.factor=sourceNode.mean
        destiNode.mean += value*self.factor
        
    def givePingjia(self,value,factor):
        print(self.value)
    
if __name__ == '__main__':
    sourceNode = node(0,0)
    destiNode = node(0,0)
    myPingjia = pingjia(sourceNode,destiNode,5)
        
