import numpy as np

rng = np.random.default_rng(seed=42)
arr = rng.uniform(0, 1, (3, 4))

# ndim:表示维度
print(arr.ndim)  # 为二维

# shape 形状
print(arr.shape)

# size 数据量
print(arr.size)

# 返回最大值
# 1. 所有元素中最大
print(arr.max())
print(arr.min())

# 2. 维度（行、列）中最大/小值
print(arr.max(axis=0))  # 列
print(arr.max(axis=1))  # 行
print(arr.max(axis=1, keepdims=True))  # 保持原有维度
print(np.amax(arr, axis=0))

# 3. 中位数
np.median(arr)  # 分位数为 1/2 时

# 4. 分位数
np.quantile(arr, q=0.25, axis=0)  # 按列取1/4数
np.quantile(arr, q=0.75, axis=1, keepdims=True)  # 按行取 3/4，同时保持维度

# 5. 平均值
np.average(arr)
np.average(arr, axis=0)  # 按列求平均值

# 6. 求和
np.sum(arr)
np.sum(arr, axis=1, keepdims=True)

# 累计求和
np.cumsum(arr)
np.cumsum(arr, axis=0)  # 按列累计求和

# 7. 方差
np.var(arr, axis=1)

# 标准差
np.std(arr, axis=1)
