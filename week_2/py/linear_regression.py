import numpy as np
import pandas as pd


# 读取数据，构成矩阵
def matrix(path):
    data_read = pd.read_csv(path)
    list = data_read.values.tolist()
    data = np.array(list)

    print(data.shape)
    return data


# 最小二次法


"""
x是输入矩阵
y是输出矩阵
matrix_w是系数矩阵
"""


def ordinary_least_squares(x, y):
    global x_1  # 全局变量，以便下一个函数还可以利用
    x = np.array(x)
    y = np.array(y)

    assert x.shape[0] == y.shape[0]  # 要求x和y的个数相同
    e = np.ones((506, 1))  # 单位矩阵
    x_1 = np.hstack((e, x))  # 合并单位矩阵和输入矩阵x，成x_1

    try:  # 判断
        matrix_w = np.dot(np.dot(np.linalg.inv(np.dot(x_1.T, x_1)), x_1.T), y)  # 不要搞反矩阵相乘的顺序！！！
    except:
        print("错误")
    else:
        return matrix_w


# 梯度下降法


"""
alpha    学习率
num_max  最大迭代次数
"""


def steepest_descent(x, y, k, alpha, num_max):
    global x_1
    x = np.array(x_1)
    y = np.array(y)
    k = np.array(k)     # k是误差函数的系数矩阵
    m = len(y)          # m为了获取输出矩阵y的维度

    try:
        steepest = np.dot(x.T, (np.dot(x, k) - y)) / m   # 计算梯度，即x的转置与kx-y（kx-y也可以看作为误差）相乘再除以m
    except:
        print("FALSE")
    else:
        for i in range(num_max):
            k -= alpha * steepest                             # 这个学习率和次数，我确实不会设。。。。。

    return k


if __name__ == '__main__':        # 内部调用，以便调试
    x = matrix('./house_price_x.csv')
    y = matrix('./house_price_y.csv')
    matrix_w = ordinary_least_squares(x, y)
    x_min = steepest_descent(x, y, matrix_w, alpha=0.2, num_max=100)
    print("最小二次法:\n",matrix_w)
    print("x_min:\n", x_min)
