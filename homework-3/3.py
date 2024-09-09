import numpy as np
import matplotlib.pyplot as plt
import matplotlib

loaded_data = np.load(r"E:\学习资料\二春\python科学计算\实验二\data\iris.npz", allow_pickle=True)
kdata, kfeature_names = loaded_data.keys()
print(loaded_data[kfeature_names])
print(loaded_data[kdata])
data = loaded_data[kdata]
matplotlib.rcParams['font.family'] = 'KaiTi'
plt.figure(figsize=(8, 8))
plt.suptitle("鸢尾花多散点图一览", fontsize=20, y=0.93, fontproperties='FangSong')
colors = ['red', 'yellowgreen', 'lightskyblue']

plt.subplot(2, 2, 1)
speal_len_setosa = data[[i for i in range(50)], 0]
speal_len_versicolor = data[[i for i in range(50, 100)], 0]
speal_len_virginica = data[[i for i in range(100, 150)], 0]
petal_len_setosa = data[[i for i in range(50)], 2]
petal_len_versicolor = data[[i for i in range(50, 100)], 2]
petal_len_virginica = data[[i for i in range(100, 150)], 2]
plt.scatter(speal_len_setosa, petal_len_setosa, c='red')
plt.scatter(speal_len_versicolor, petal_len_versicolor, c='yellow')
plt.scatter(speal_len_virginica, petal_len_virginica, c='green')
plt.xlabel("萼片长度")
plt.ylabel("花瓣长度")
plt.legend(['山鸢尾', '变色鸢尾', '弗吉尼亚'])

plt.subplot(2, 2, 2)
speal_wid_setosa = data[[i for i in range(50)], 1]
speal_wid_versicolor = data[[i for i in range(50, 100)], 1]
speal_wid_virginica = data[[i for i in range(100, 150)], 1]
petal_wid_setosa = data[[i for i in range(50)], 3]
petal_wid_versicolor = data[[i for i in range(50, 100)], 3]
petal_wid_virginica = data[[i for i in range(100, 150)], 3]
plt.scatter(speal_wid_setosa, petal_wid_setosa, c='red')
plt.scatter(speal_wid_versicolor, petal_wid_versicolor, c='yellow')
plt.scatter(speal_wid_virginica, petal_wid_virginica, c='green')
plt.xlabel("萼片宽度")
plt.ylabel("花瓣宽度")
plt.legend(['山鸢尾', '变色鸢尾', '弗吉尼亚'])

plt.subplot(2, 2, 3)
plt.scatter(speal_len_setosa, speal_wid_setosa, c='red')
plt.scatter(speal_len_versicolor, speal_wid_versicolor, c='yellow')
plt.scatter(speal_len_virginica, speal_wid_virginica, c='green')
plt.xlabel("萼片长度")
plt.ylabel("萼片宽度")
plt.legend(['山鸢尾', '变色鸢尾', '弗吉尼亚'])

plt.subplot(2, 2, 4)
plt.scatter(petal_len_setosa, petal_wid_setosa, c='red')
plt.scatter(petal_len_versicolor, petal_wid_versicolor, c='yellow')
plt.scatter(petal_len_virginica, petal_wid_virginica, c='green')
plt.xticks(range(1, 8))
plt.xlim(0.5, 7.2)
plt.xlabel("花瓣长度")
plt.ylabel("花瓣宽度")
plt.legend(['山鸢尾', '变色鸢尾', '弗吉尼亚'])
plt.show()