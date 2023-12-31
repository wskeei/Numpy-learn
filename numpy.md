## PCG64
伪随机数生成器，用于生成随机数序列。
是LCG变种

## 文件
* .npy：用于存储单个NumPy数组的数据。
* .npz: 用于存储多个NumPy数组，以及这些数组的名称。

## 分位数

假如有1000个数字(正数)，这些数字的5%, 30%, 50%, 70%, 99%分位数分别是 [3.0,5.0,6.0,9.0,12.0]，这表明有5%的数字分布在0-3.0之间，有25%的数字分布在3.0-5.0之间，有20%的数字分布在5.0-6.0之间，有20%的数字分布在6.0-9.0之间，有29%的数字分布在9.0-12.0之间，有1%的数字大于12.0，这就是分位数的统计学理解


## 维度
* 一维数组 
`a = np.array([0, 1, 2, 3])  一维 长为4 shape: (4,)`

* 二维数组 
```
          b = np.array([[ 0,  1,  2,  3],
                        [ 4,  5,  6,  7],
                        [ 8,  9, 10, 11]])
二维 长为3宽为4 shape:(3,4)
axis=0 为 向下 行 3
axis=1 为 向右 列 4 
```

* 三维数组 本质是二维数组堆叠形成的 
``` 
            c = np.array([[[ 0,  1,  2,  3],
                           [ 4,  5,  6,  7],
                           [ 8,  9, 10, 11]],
                           
                          [[12, 13, 14, 15],
                           [16, 17, 18, 19],
                           [20, 21, 22, 23]],
                           
                          [[24, 25, 26, 27],
                           [28, 29, 30, 31],
                           [32, 33, 34, 35]]])
  3维 深度为3长为3宽为4 shape:(3,3,4)
  
巧记：右下里，依次递减。
解释：
最高维的轴朝右 axis = 2
第二个轴朝下 axis = 1
第三个轴朝里 axis = 0
```

## numpy.expand_dims(a, axis)
在数组 a 的特定轴上增加一个新的维度。
这个函数可以用来改变数组的形状，使得在某个轴上增加一个新的维度。

  
  