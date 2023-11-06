import numpy as np
import matplotlib.pyplot as plt

a = np.arange(100, 124, 2).reshape(3, 2, 2)

b = np.linspace(0, 9, 5, endpoint=True)  # (9-0)/4 四个间隔
c = np.linspace(0, 9, 5, endpoint=False)  # （9-0）/5 五个间隔 但是不取第五个
# print(b, c)

# logspace :用于创建以base为底数的start次幂到stop次幂的等比数列，包含num个元素，默认base为10
# 1.02400000e+03：为 1.024 乘 10 的 3 次方 即1024
y2 = np.logspace(0, 10, 20, base=2)

# print(f'y2={y2}')

# ones/zeros: 创建全为1/0的快捷方式，默认为float类型
ones = np.ones((2, 3, 3))  # 两行三列 每个位置中有3个元素
zl = np.zeros_like(ones)
# print(ones, zl)

# 0-1均匀分布
rand = np.random.rand(2, 3)
random = np.random.random((2, 3))
np.random.uniform(-1, 1, (2, 3))
# print(rand)

rng = np.random.default_rng(42)  # 42 seed
# print(rng)

# 连续均匀分布
# print(rng.random((2, 3)))
# print(rng.uniform(-1, 1, (2, 3))) # 指定上下界

# 离散均匀分布
# print(np.random.randint(1, 10, 9)) # 生成范围内的随机整数
# print(rng.integers(1, 10, 9))

# 标准正态分布
# print(np.random.randn(2, 4))  # 标准正态分布 2行4列
# print(rng.standard_normal((2, 4)))

# 高斯分布 即正态分布
# print(np.random.normal(0, 1, (3, 5)))
# print(rng.normal(0, 1, (3, 5)))

# 文件操作
# np.save('./a', rng.normal(0, 1, (3, 5))) #保存
# print(np.load("./a.npy")) #加载

# np.savez("./b.npz", a=np.arange(12), b=np.arange(10))
# arr = np.load("./b.npz")
# print(arr["a"])
