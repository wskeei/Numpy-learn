import numpy as np

rng = np.random.default_rng(seed=42)
arr = rng.integers(1, 100, (3, 4))

print(arr)
# 将多维数组一行输出
print(arr.ravel())

# 扩展 1 个维度，需要（必须）指定维度
print(np.expand_dims(arr, 1))

