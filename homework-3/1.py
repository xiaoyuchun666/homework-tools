import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
matplotlib.rcParams['font.family']='FangSong'
datas=np.load("E:\学习资料\二春\python科学计算\实验二\data\populations.npz",allow_pickle=True)
data=datas['data']
y=datas['feature_names']
df=pd.DataFrame(data=data,index=None,columns=y,dtype=None)
df.dropna(axis=0,how='all',inplace=True)
df.sort_values(by=['时间'],axis=0,ascending=True,inplace=True)
plt.figure(figsize=(8,4))
a=df['时间']
b=df['年末总人口(万人)']
c=list()
for i in range(len(a)):
    c.append(float(a[i].rstrip("年")))
c.sort()
plt.plot(c,b,'ko--')
plt.xlabel("年份")
plt.ylabel("总人口")
xlable = list(range(1996, 2016, 4))
xl = [str(i) + "年" for i in xlable]
plt.xticks(xlable, xl)
plt.title("总人口线形图")
plt.legend(["总人口"])
plt.show()