import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
import heapq
for i in range(2,6):
    for j in range(1,i+1):
        name = 'c'+ str(i)+'exm'+str(j)+'.txt'
        file=pd.read_csv(name,encoding='gbk')
        file_x = file['x']
        file_y = file['y']
        plt.scatter(file_x, file_y, s=50)
        plt.scatter(sum(file_x)/len(file_x), sum(file_y)/len(file_y), s=100)
        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
    plt.show()
