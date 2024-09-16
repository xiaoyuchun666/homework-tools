
import random
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import DataLoader, TensorDataset

# 超参数
batch_size = 32
learning_rate = 0.001
num_epochs = 10
num_samples = 1000
num_features = 20
num_classes = 3

# 随机生成数据集
np.random.seed(0)
X = np.random.rand(num_samples, num_features).astype(np.float32)  # 特征
y = np.random.randint(0, num_classes, size=(num_samples,)).astype(np.int64)  # 标签

# 创建 TensorDataset 和 DataLoader
dataset = TensorDataset(torch.from_numpy(X), torch.from_numpy(y))
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 定义神经网络
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(num_features, 64)  # 输入层到隐藏层
        self.fc2 = nn.Linear(64, 32)              # 隐藏层到隐藏层
        self.fc3 = nn.Linear(32, num_classes)     # 隐藏层到输出层

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 激活函数
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 实例化模型、损失函数和优化器
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 训练模型
for epoch in range(num_epochs):
    for images, labels in train_loader:
        optimizer.zero_grad()  # 清零梯度
        outputs = model(images)  # 前向传播
        loss = criterion(outputs, labels)  # 计算损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新参数

    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

print("Training complete!")
