import numpy as np

rng = np.random.default_rng(seed=42)
arr = rng.integers(1, 100, (3, 4))

# print(arr)
# 将多维数组一行输出
# print(arr.ravel())

# 扩咱维度
# 扩展 1 个维度，需要（必须）指定维度
exp = np.expand_dims(arr, 1)  # 在第一个维度上进行扩展
# print(exp.shape)
# print(exp)

expanded = np.expand_dims(arr, axis=(1, 3, 4))  # 在1,3,4维度上进行扩展
# print(expanded.shape)

# 扩充维度不能跳跃
# expanded = np.expand_dims(arr, axis=(1, 3, 8)) # 会失败

# np.squeeze 从数组中移除维度大小为1的维度
np.squeeze(expanded, axis=1).shape  # 第一维度大小为1,使用squeeze去除

# 去除数组中所有维度大小为1
np.squeeze(expanded).shape

# np.reshape/arr.reshape
arr.reshape(2, 2, 3)
arr1 = arr.reshape((4, -1))  # -1为占位符，会自动计算具体数字为多少，这里为3

# resize 同样可以用来改变数组的形状，
# 相比于reshape，resize可以数组的形状并且可以增加或减少元素的数量
# 如果需要增加元素的数量，它会根据指定的填充值来填充新的元素，默认为0
arr.resize((4, 5), refcheck=False)
# refcheck 设为 False 此时 arr 会发生变化,元素数量超出时，会截断；元素数量不够时，0填充

# print(arr)
c = np.resize(arr, (5, 3))

b = np.resize(arr, (4,5))

# 反序
s = "uevol"
s[::-1] # 字符串反序

arr[::-1] # 默认情况 数组列反序

arr[::-1, :] # 列不变，行反序

arr[:, ::-1] # 行不变列反序

arr[::-1, ::-1] # 行列均反序

# 转置
# 二维矩阵用 arr.T （快）
# 超过二维的张量可以用 np.transpose，（ 更加灵活 ）

np.array([1,2]).T # 一维数组转序 还是自己

arr.T #  转置

arr.reshape(1, 1, 3, 4).T.shape # 结果为 (4, 3, 1, 1)

np.transpose(arr)

# transpose 可以自定义轴的顺序 即axes参数
# axes 数量必须包含所有维度的序列
np.transpose(arr.reshape(1, 1, 3, 4), axes=(0, 2, 1, 3)).shape
# 结果为 (1, 3, 1, 4)