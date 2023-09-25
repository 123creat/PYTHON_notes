import pandas as pd
import numpy as np
scenery_file_path=open(r'F:\jupyter'
                      r'/�羰��ʤ��.csv')
scenery_data=pd.read_csv(scenery_file_path)
scenery_data
area=float("{:.lf}".format(
    scenery_data['�������ƽ��ǧ�ף�'].mean()))
tourist=float("{:.l}".format(
     scenery_data['�ο��������˴Σ�'].mean()))
values={"�������ƽ��ǧ�ף�":area,"�ο��������˴Σ�":tourist}
scenery_data=scenery_data.fillna(value=values)
scenery_data.head

data=scenery_data.groupby("ʡ��")
hebei_scenery=dict([x for x in data])['�ӱ�']
hebei_scenery

import matplotlib.pyplot as plt
matplotlib inline
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
area=hebei_scenery['�����(ƽ��ǧ��)'].values
tourist=hebei_scenery['�ο���(���˴�)'].values
plt.figure(figsize=(12,6))
x_num=range(0,len(area))
x_dis=[i + 0.3 for i in x_num]
plt.bar(x_num,area,color='g',width=.3,label='�����')
plt.bar(x_dis,tourist,color='r',width=.3,label='�ο���')
plt.ylabel('��λ:ƽ��ǧ��/���˴�')
plt.title('�ӱ�����������ο�����')
plt.legend(loc='upper right')
plt.xticks(range(0,10),['����ɽ','��ʯ��','������-���ɽ','�ػʵ�������','����ɽ',
                       '活ʹ�','̫�д�Ͽ��','��ɽ���ƶ�','Ұ����','�е±���ɽׯ�����'])
plt.show()

import matplotlib.pyplot as plt
every_scenery=hebei_scenery['�����(ƽ��ǧ��)'].values
all_scenery=hebei_scenery['�ο���(���˴�)'].sum()
percentage=(every_scenery/all_scenery)*100
np.set_printoptions(precision=2)
labels=['����ɽ','��ʯ��','������-���ɽ','�ػʵ�������','����ɽ',
                       '活ʹ�','̫�д�Ͽ��','��ɽ���ƶ�','Ұ����','�е±���ɽׯ�����']
plt.axes(aspect=1)
plt.pie(x=percentage,labels=labels,autopct='%3.2f %%',
       shadow=True,labeldistance=1.2,startangle=90,pctdistance=0.7)
plt.legend(loc='left')
plt.show()