#coding=utf-8
__author__ = 'shuai'
import sys
import numpy as np
from numpy import *
reload(sys)
sys.setdefaultencoding('utf-8')
def xiaoYuan(a,b):
    x=linalg.solve(a,b)
    return x
a=np.mat([[8.0,-3.0,2.0],[4.0,11.0,-1.0],[6.0,3.0,12.0]])
b=np.mat([[20.0],[33.0],[36.0]])
x=xiaoYuan(a,b)
print 'result=',x