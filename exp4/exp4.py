from cffi.backend_ctypes import xrange
from numpy import *
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
import heapq

# sigmoid函数
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


x = np.arange(-10, 10, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.show()

#梯度下降算法
def trainLogRegres(train_x, train_y, opts):
    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha']
    maxIter = opts['maxIter']
    weights = ones((numFeatures, 1))

    # optimize through gradient descent algorilthm
    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':  # gradient descent algorilthm
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
            print(weights)

    return weights


# 验证数据在哪个区域
def testLogRegres(weights, test_x):
    numSamples, numFeatures = shape(test_x)

    matchCount = 0
    for i in xrange(numSamples):
        if sigmoid(test_x[i, :] * weights)[0, 0] > 0.5:
            return 1
        else:
            return 0


#画图
def showLogRegres(weights, train_x, train_y):
   
    numSamples, numFeatures = shape(train_x)

    #画出所有点
    for i in xrange(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')

    # 画出分割线
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0] #最大最小x
    weights = weights.getA()  
    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
    #根据weights得到相应的y
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def loadData():
    train_x = []
    train_y = []
    fileIn = open('marked.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()


print("步骤一：导入数据")
train_x, train_y = loadData()
test_x = []
test_x.append([1,6,2])
test_x = mat(test_x)



print("步骤二：训练")
opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'gradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)

print("步骤三：显示结果(6,2)所在的区域为：",testLogRegres(optimalWeights, test_x))
print("在图中的位置为")
plt.scatter(6,2,s=150,c='r')


print("步骤四：画图")
showLogRegres(optimalWeights, train_x, train_y)
