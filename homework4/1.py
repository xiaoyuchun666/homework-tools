import torch
import numpy as np
# 创建一个 5*3 的矩阵
x = torch.empty(5, 3)
print(x)

# 创建一个随机初始化的 5*3 矩阵
rand_x = torch.rand(5, 3)
print(rand_x)

# 创建一个数值皆是 0，类型为 long 的矩阵
zero_x = torch.zeros(5, 3, dtype=torch.long)
print(zero_x)

# tensor 数值是 [5.5, 3]
tensor1 = torch.tensor([5.5, 3])
print(tensor1)

# 显示定义新的尺寸是 5*3，数值类型是 torch.double
tensor2 = tensor1.new_ones(5, 3, dtype=torch.double)  # new_* 方法需要输入 tensor 大小
print(tensor2)

# 修改数值类型
tensor3 = torch.randn_like(tensor2, dtype=torch.float)
print('tensor3: ', tensor3)

tensor4 = torch.rand(5, 3)
print('tensor3 + tensor4= ', tensor3 + tensor4)
print('tensor3 + tensor4= ', torch.add(tensor3, tensor4))
# 新声明一个 tensor 变量保存加法操作的结果
result = torch.empty(5, 3)
torch.add(tensor3, tensor4, out=result)
print('add result= ', result)
# 直接修改变量
tensor3.add_(tensor4)
print('tensor3= ', tensor3)

# 访问 tensor3 第一列数据
print(tensor3[:, 0])

x = torch.randn(4, 4)
y = x.view(16)
# -1 表示除给定维度外的其余维度的乘积
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())

#Tensor 与 Numpy 数组互换
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)