import scipy.io
import numpy as np

# 加载数据
data = scipy.io.loadmat('D:\\机器学习\\神经网络\\前向传播\\ex3data1.mat')

# 查看里面有什么
X = data['X'] # 特征数据
y = data['y'] # 标签

a = [[1,2,3],[1,2,3]]
print(len(a))