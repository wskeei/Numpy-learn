import numpy as np

# 切片索引
rng = np.random.default_rng(42)
arr = rng.integers(0, 20, (5, 4))

# index/slice
# print(arr)

# 每个维度均为 start:stop:step

# print(arr[0:3, 0:2])  # 行，列  取 0-2行 0-1列

# print(arr[:, 1])  # 不处理的维度用 : 或 ... 代替

# print(arr[[0, 3]])  # 离散取行

# 拼接 使用np.concatenate
rng = np.random.default_rng(42)

arr1 = rng.random((2, 3))
arr2 = rng.random((2, 3))

np.concatenate((arr1, arr2))  # 默认沿axis=0（列）连接
np.concatenate((arr1, arr2), axis=1)  # 沿 axis=1（行）连接

np.vstack((arr1, arr2))  # 竖直按行顺序拼接 和concatenate相同 不建议使用

np.hstack((arr1, arr2))  # 水平按列顺序拼接 和concatenate相同 不建议使用

# 堆叠 （会增加一个维度）

a = np.stack((arr1, arr2))  # 堆叠，默认根据 axis=0 进行
print(a.shape)  # (2,2,3)
np.stack((arr1, arr2), axis=2)  # 堆叠，根据 axis=2


# 重复 （重复是一个维度一个维度依次重复，而不是整个 array 重复。）

rng = np.random.default_rng(42)
np.repeat(arr, 2, axis=0)  # 在 axis=0（沿着列）上重复 2 次
np.repeat(arr, 3, axis=1)  # 在 axis=1（沿着行）上重复 3 次


# 分拆 （将 array 拆成想要的几份）
np.split(arr, 3)  # 默认切分列（axis=0），切成 3 份
np.split(arr, 2, axis=1)  # （axis=1）切分行


