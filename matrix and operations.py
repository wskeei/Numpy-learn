import numpy as np

rng = np.random.default_rng(42)
arr = rng.integers(1, 20, (3, 4))

arr * 2  # +-*/ 四则运算
arr ** 2  # 平方
np.sqrt(arr)  # 开方
np.log(arr)  # log
np.minimum(arr, 5)  # 超过5的都换成5
np.maximum(arr, 5)  # 低于5的都换成5c

np.round(np.sqrt(arr), 2)
np.floor(np.sqrt(arr))  # 向下取整,即去小数部分,返回小于或等于原数的最大整数。
np.ceil(np.sqrt(arr))  # 向上取整,即舍去小数部分,返回大于或等于原数的最小整数。

np.mod(arr, 3)  # mod <=> x % 3
arr - 5  # 每一个都-5
np.mod(arr, arr - 5)  # 使用多个被除数

# 广播
a = rng.integers(1, 100, (3, 4))
a + [1, 2, 3, 4]  # 广播，后面的被当做 1 行 4 列
a + [[1], [2], [3]]  # 后面的被当做 3 行 1 列
np.mod(a, [1, 2, 3, 4])  # 取余也可以实现

# 矩阵
rng = np.random.default_rng(42)
a = rng.integers(1, 10, (3, 2))
b = rng.integers(1, 10, (2, 4))
c = rng.integers(1, 10, (3, 3))

# 乘法
np.dot(a, b)
a.dot(b)

np.matmul(a, b)  # 与 dot 的主要区别是：matmul 矩阵（好像元素一样）堆叠在一起广播
# dot和matmul在高维度表现不同
a @ b  # 写起来比较好看的方法

# 点积
np.vdot(a, a)
np.sum(a*a)

# 内积
np.sum(a*a)
np.inner(a, a)
a.dot(a.T)

# 行列式
np.linalg.det(c)

# 逆矩阵（方阵）
np.linalg.inv(c)



