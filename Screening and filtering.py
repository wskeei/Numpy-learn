import numpy as np

# 从「整体」中统一筛选出「符合条件」的内容
rng = np.random.default_rng(42)
# arr = rng.integers(1, 100, (3, 4))

# 条件筛选

# print(arr > 50)
# print(np.where(arr > 50))  # 返回满足条件的索引 两个维度输出两个结果
# np.where(arr > 50, arr, -1)  # 不满足条件的赋值，将 <=50 的替换为 -1

# 提取 提取指定条件的值。
# 提取和唯一值返回的都是一维向量。

# np.extract(arr > 50, arr)  # 提取指定条件的值
# np.unique(arr)  # 唯一值，是另一种形式的提取

# 抽样

# 第一个参数是要抽样的集合，如果是一个整数，则表示从 0 到该值
# 第二个参数是样本大小
# 第三个参数表示结果是否可以重复
# 第四个参数表示出现的概率，长度和第一个参数一样
# 由于（0 1 2 3）中 2 和 3 的概率比较高，自然就选择了 2 和 3
# rng = np.random.default_rng(42)
rng.choice(4, 2, replace=False, p=[0.1, 0.2, 0.3, 0.4])


# 旧的 API
# 如果是抽样语料的 index，更多的方法是这样：
data_size = 10000
np.random.choice(data_size, 50, replace=False)

# 最值
arr = rng.uniform(1, 100, (3, 4))

# argmax/argmin
np.argmax(arr)  # 所有值中最大值的 Index，基本不这么用
np.argmax(arr, axis=0)  # 按列（axis=0）最大值的 Index
np.argmin(arr, axis=1)  # 按行（axis=1）最小值的 Index

# argsort
np.argsort(arr)  # 默认按行（axis=1）排序的索引
np.argsort(arr, axis=1)  # 数据按行（axis=1）排序的索引，同上

np.argsort(arr, axis=0)  # 数据按列（axis=0）排序索引

