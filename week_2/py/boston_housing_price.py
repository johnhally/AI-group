import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import linear_regression as lr   # 引用实现线性回归函数的库

# 读入数据
# f = open(r'./house_price.csv')
f = pd.read_csv(open('./house_price.csv', 'r', encoding='utf-8'))
df = pd.DataFrame(f)

# 数据查看
print("describe:", df.describe(include='all'), '\n')
print("info:", df.info, '\n')
print("shape:", df.shape, '\n')
print(df.dtypes, '\n')
print("keys:", df.keys(), '\n')

# 检测与处理重复值
is_repeat = df.drop_duplicates(subset=None, keep='first', inplace=False)
print('检测重复\n')
print(is_repeat, '\n')

# 检测缺失值并删去含缺失值所在的行
is_lack = df.isnull().sum()
df.dropna(inplace=True)
print('检测缺失')
print(is_repeat, '\n')

# 计算各因数与房价的相关性
corr_matrix = df.corr()
effect_of_boston_price = corr_matrix['medv'].sort_values(ascending=False)
print("相关性:\n",effect_of_boston_price)

# 数据可视化
rng = np.random.RandomState(0)  # 使用RandomState获得随机数生成器，（）里的数字不同便代表着不同组数据，好像没特别意义

colors = rng.rand(506)  # 随机产生506（506个数据）个用于颜色映射的数值，用多或少了还报错
sizes = 700 * rng.rand(506)  # 随机产生506（506个数据）个用于改变散点面积的数值，用多或少了还报错
plt.scatter(df['rm'], df['medv'], c=colors, s=sizes, alpha=0.3, cmap='viridis')

plt.title("住宅房间数对房价的影响", fontproperties="SimHei")
plt.xlabel("住宅房间数（间）", fontproperties="SimHei")  # 必须要个fontproperties="SimHei"，要不然用不了中文
plt.ylabel("住宅房价中间值（X1000美元）", fontproperties="SimHei")
plt.colorbar()
plt.show()

plt.scatter(df['b'], df['medv'], c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.title("黑人邻居对房价的影响", fontproperties="SimHei")
plt.xlabel("黑人占比", fontproperties="SimHei")
plt.ylabel("住宅房价中间值（X1000美元）", fontproperties="SimHei")
plt.colorbar()
plt.show()

plt.scatter(df['zn'], df['medv'], c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.title("住宅用地所占比例对房价的影响", fontproperties="SimHei")
plt.xlabel("住宅用地占比比例", fontproperties="SimHei")
plt.ylabel("住宅房价中间值（X1000美元）", fontproperties="SimHei")
plt.colorbar()
plt.show()

pd.plotting.scatter_matrix(df, figsize=(12, 8))  # pandas中scatter_matrix函数，它会绘制出每个数值属性相对于其他数值属性的相关值。
plt.show()
df.hist(bins=50, figsize=(20, 15))  # 画直方图
plt.show()

# 线性回归
x = lr.matrix('./house_price_x.csv')
y = lr.matrix('./house_price_y.csv')

matrix_k = lr.ordinary_least_squares(x, y)
x_min = lr.steepest_descent(x, y, matrix_k, alpha=0.2, num_max=100)

print("最小二次法:\n",matrix_k)
print("x_min:\n", x_min)