#coding=utf-8
__author__ = 'shuai'
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

#求解ax=b的x的解
def biJin(a,b):
    size=len(a)
    B=np.copy(a)
    #print B
    f=np.copy(b)
    x=np.mat([[0],[0],[0]])
    #求出变换后的B和f-->x=Bx+f
    for i in range(size):
        for j in range(size):
            #print i,j
            if i==j:
                B[i,j]=0
            else:
                B[i,j]=-B[i,j]/a[i,i]
    for i in range(size):
        f[i]=f[i]/a[i,i]
    print 'B=',B
    print 'f=',f.T
    for i in range(20):
        #print 'b*x=',B*x
        x=B*x+f
        print 'x=',x
    return x
a=np.mat([[8.0,-3.0,2.0],[4.0,11.0,-1.0],[6.0,3.0,12.0]])
b=np.mat([[20.0],[33.0],[36.0]])
x=biJin(a,b)
print 'result=',x
