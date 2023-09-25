import pandas as pd
import numpy as np
scenery_file_path=open(r'F:\jupyter'
                      r'/风景名胜区.csv')
scenery_data=pd.read_csv(scenery_file_path)
scenery_data
area=float("{:.lf}".format(
    scenery_data['总面积（平方千米）'].mean()))
tourist=float("{:.l}".format(
     scenery_data['游客量（万人次）'].mean()))
values={"总面积（平方千米）":area,"游客量（万人次）":tourist}
scenery_data=scenery_data.fillna(value=values)
scenery_data.head

data=scenery_data.groupby("省份")
hebei_scenery=dict([x for x in data])['河北']
hebei_scenery

import matplotlib.pyplot as plt
matplotlib inline
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
area=hebei_scenery['总面积(平方千米)'].values
tourist=hebei_scenery['游客量(万人次)'].values
plt.figure(figsize=(12,6))
x_num=range(0,len(area))
x_dis=[i + 0.3 for i in x_num]
plt.bar(x_num,area,color='g',width=.3,label='总面积')
plt.bar(x_dis,tourist,color='r',width=.3,label='游客量')
plt.ylabel('单位:平方千米/万人次')
plt.title('河北景点面积及游客数量')
plt.legend(loc='upper right')
plt.xticks(range(0,10),['苍岩山','嶂石岩','西柏坡-天桂山','秦皇岛北戴河','响堂山',
                       '娲皇宫','太行大峡谷','崆山白云洞','野三坡','承德避暑山庄外八庙'])
plt.show()

import matplotlib.pyplot as plt
every_scenery=hebei_scenery['总面积(平方千米)'].values
all_scenery=hebei_scenery['游客量(万人次)'].sum()
percentage=(every_scenery/all_scenery)*100
np.set_printoptions(precision=2)
labels=['苍岩山','嶂石岩','西柏坡-天桂山','秦皇岛北戴河','响堂山',
                       '娲皇宫','太行大峡谷','崆山白云洞','野三坡','承德避暑山庄外八庙']
plt.axes(aspect=1)
plt.pie(x=percentage,labels=labels,autopct='%3.2f %%',
       shadow=True,labeldistance=1.2,startangle=90,pctdistance=0.7)
plt.legend(loc='left')
plt.show()