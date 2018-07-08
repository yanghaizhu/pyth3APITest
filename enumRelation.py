#!/usr/bin/env python
#coding:utf8

from enum import Enum, unique


@unique
class enumRelation(Enum):
    isPartOf = 1
    isSameAs = 2
    isRefine = 3      #shengwu dongwu ren
    isProduceOf = 4
    isConsumerOf = 5
    isMaterialOf = 6
    isDescriptionOf = 7
    isPropertyOf = 8
