
#coding=utf-8
__author__ = 'shuai'
import sys,random
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import matplotlib.pyplot as plt
#time=x0+cit*num
#diff=alf*()
x= [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0, 120.0, 121.0, 122.0, 123.0, 124.0, 125.0, 126.0, 127.0, 128.0, 129.0, 130.0, 131.0, 132.0, 133.0, 134.0, 135.0, 136.0, 137.0, 138.0, 139.0, 140.0, 141.0, 142.0, 143.0, 144.0, 145.0, 146.0, 147.0, 148.0, 149.0, 150.0, 151.0, 152.0, 153.0, 154.0, 155.0, 156.0, 157.0, 158.0, 159.0, 160.0, 161.0, 162.0, 163.0, 164.0, 165.0, 166.0, 167.0, 168.0, 169.0, 170.0]
y= [0.0, 28.546, 31.89, 39.312, 41.787, 46.489, 47.744, 70.727, 75.397, 92.559, 105.15, 124.376, 126.197, 143.04, 149.881, 152.914, 154.189, 162.034, 167.652, 168.924, 189.32, 195.956, 207.682, 215.096, 220.38, 220.402, 227.969, 228.3, 249.454, 267.472, 272.066, 275.431, 284.215, 289.76, 298.257, 327.553, 327.575, 330.467, 334.821, 343.224, 343.447, 402.625, 406.156, 432.64, 465.652, 467.311, 501.672, 525.679, 528.97, 555.688, 555.937, 573.692, 600.7, 630.708, 633.708, 645.746, 693.776, 708.78, 711.809, 738.791, 768.811, 771.898, 798.818, 803.872, 828.826, 831.943, 864.837, 873.839, 877.102, 890.088, 936.855, 941.603, 951.873, 956.575, 996.872, 1008.883, 1026.893, 1056.904, 1081.066, 1105.611, 1117.596, 1126.445, 1131.049, 1135.407, 1165.167, 1181.844, 1183.995, 1193.284, 1193.817, 1196.204, 1205.568, 1206.042, 1207.296, 1219.607, 1221.218, 1223.92, 1232.189, 1236.957, 1237.627, 1243.343, 1267.218, 1283.75, 1287.572, 1297.242, 1307.999, 1327.311, 1332.948, 1333.73, 1342.833, 1350.419, 1352.056, 1363.717, 1365.658, 1367.317, 2248.957, 2249.735, 2249.766, 2249.823, 2249.858, 2249.894, 2249.942, 2249.966, 2250.015, 2250.04, 2250.169, 2250.207, 2250.257, 2250.3, 2250.379, 2250.42, 2250.451, 2250.489, 2250.526, 2250.553, 2250.598, 2251.884, 2264.579, 2267.012, 2279.382, 2280.452, 2285.062, 2285.361, 2613.243, 2613.273, 2613.327, 2613.357, 2613.384, 2613.448, 2613.487, 2613.56, 2613.591, 2613.619, 2613.647, 2613.672, 2613.689, 2614.898, 2617.042, 2617.216, 2636.003, 2636.114, 2637.688, 2637.794, 2639.229, 2639.404, 2666.271, 2666.44, 2680.894, 2684.112, 2684.568, 2684.659]
print len(x)
print len(y)
def regress(x,y,maxCount=100,esp=0.000003,alf=0.00005):
    cit=[0,0]
    currentCount=0
    lasterr=0
    err=0
    while currentCount<maxCount:
    #更新cit
        currentCount+=1
        length=len(x)
        err=0
        for index in range(length):
                diff=y[index]-cit[0]-cit[1]*x[index]
                #print 'diff=',diff
                cit[0]=cit[0]+diff*alf
                cit[1]=cit[1]+diff*alf*x[index]
    #for citx in range(length):
        err+=diff*alf+diff*alf*x[index]
        if abs(err-lasterr)<esp:
            print 'esp',esp
            print 'currentCount=',currentCount
            print 'err-laster=',abs(err-lasterr)
            break
        lasterr=err
    print currentCount
    return cit
def showReges(plt,cits):
    plt.figure(1)
    plt.subplot(111)
    plt.plot(y,x)
    x1 = np.linspace(0, 180, 100)
    for cit in cits:
        y1=map(lambda x:x*cit[1]+cit[0],x1)
        plt.plot(y1,x1)
    plt.show()
print 'x=',x
print 'y=',y
cits=[0,0,0,0,0,0]
cits[0]=regress(x,y)
cits[1]=regress(x,y,200)
cits[2]=regress(x,y,300)
cits[3]=regress(x,y,500)
cits[4]=regress(x,y,600)
cits[5]=regress(x,y,800)
print cits
showReges(plt,cits)

print len(x)
print len(y)











