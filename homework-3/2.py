import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def outrange(ser):#进行替换
    QU=ser.quantile(upper)
    QL=ser.quantile(lower)
    IQR=QU-QL
    ser[ser > QU + whis*IQR]=QU
    ser[ser < QL - whis*IQR]=QL
    return ser
def yes(outlier,QU,QL,whis,IQR):#判断超过上界和下届的值都存在
    for item in outlier:
        for a in outlier:
            if item > QU+whis*IQR:
                if a < QL-whis*IQR:
                    return True
    return False
def cc():
    data = np.round(np.random.normal(loc=1000, scale=200, size=50), 2)
    ser1 = pd.Series(data)
    QU = ser1.quantile(upper)
    QL = ser1.quantile(lower)
    IQR = QU - QL
    p = plt.boxplot(x=ser1, notch=True, whis=1.25, labels=['DATA'])
    outlier1 = p['fliers'][0].get_ydata()
    if yes(outlier1,QU,QL,whis,IQR):
        return False
    else:
        return True
upper=0.75
lower=0.25
whis=1.25
plt.figure(figsize=(5,4))
data = np.round(np.random.normal(loc=1000, scale=200, size=50), 2)
ser1 = pd.Series(data)
QU = ser1.quantile(upper)
QL = ser1.quantile(lower)
IQR = QU - QL
p = plt.boxplot(x=ser1, notch=True, whis=1.25, labels=['DATA'])
plt.cla()
outlier1 = p['fliers'][0].get_ydata()
#循环，直到找到符合（1）要求的数据
while cc():
    plt.cla()
plt.show()#显示图
#得出index
index= ser1[ser1.isin(outlier1)].index
print('原对象：\n',ser1)
col1=ser1[index]#原始异常值
print('上四分位数QU',QU,'\n下四分位数QL',QL,'\n四分位间距IQR：',IQR)
print('异常值：',outlier1)
print('异常值索引：',index)
ser1=outrange(ser1)#进行替换
print('替换后的对象：\n',ser1)
col2=ser1[index]#替换后的值
df=pd.DataFrame({'Before':col1,'After':col2},index=index)
print(df)





