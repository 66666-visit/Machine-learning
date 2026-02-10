# Machine Learning Journey 🤖

![Language](https://img.shields.io/badge/language-Python-blue.svg)
![Jupyter](https://img.shields.io/badge/Tool-Jupyter%20Notebook-orange.svg)
![Status](https://img.shields.io/badge/Status-Learning-green.svg)

## 简介 (Introduction)

本仓库用于记录我学习 **机器学习 (Machine Learning)** 过程中的代码实践、笔记与心得。
内容涵盖了从基础的监督学习（回归、分类）到无监督学习（聚类），以及神经网络的初步探索。

每个文件夹对应一个特定的算法或主题，包含理论实现与实战案例。

## 目录结构 (Contents)

为了方便索引，我将学习内容按算法类别进行了分类：

### 📈 监督学习 - 回归 (Regression)
* **[线性回归 (Linear Regression)](./线性回归)**
    * 基础的单变量与多变量线性回归实现。
    * 梯度下降法 (Gradient Descent) 的应用。
* **[多项式回归 (Polynomial Regression)](./多项式回归)**
    * 处理非线性数据的回归方法。
    * 学习曲线与过拟合/欠拟合的分析。

### 🏷️ 监督学习 - 分类 (Classification)
* **[逻辑回归 (Logistic Regression)](./逻辑回归)**
    * 用于二分类问题的基础算法。
    * 决策边界的可视化。
* **[打造实用机器学习系统](./打造实用机器学习系统)**
    * 是关于模型评估、偏差与方差分析、以及如何构建完整 ML 流程的实践记录。

### 🧠 深度学习基础 (Deep Learning Basics)
* **[神经网络 (Neural Networks)](./神经网络)**
    * 前馈神经网络 (Feedforward Neural Network) 的实现。
    * 反向传播算法 (Backpropagation) 的理解与代码。

### 🧩 无监督学习 (Unsupervised Learning)
* **[聚类算法 (Clustering)](./聚类算法)**
    * K-Means 聚类算法的实现。
    * 数据降维与分组探索。

## 技术栈 (Tech Stack)

* **编程语言**: Python 3.x
* **核心工具库**:
    * `NumPy`: 矩阵运算与数值处理
    * `Pandas`: 数据清洗与操作
    * `Matplotlib` / `Seaborn`: 数据可视化与结果展示
    * `Scikit-learn`: 机器学习算法库
    * `SciPy`: 科学计算工具

## 使用说明 (Usage)
1.  **环境准备**:
    建议安装 Anaconda 或 Miniconda，并创建一个新的虚拟环境。
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn jupyter
    ```
2.  **运行代码**:
    进入对应目录，启动 Jupyter Notebook：
    ```bash
    jupyter notebook
    ```
---
*Stay Hungry, Stay Foolish.* 🌱
