import numpy as np
import os
import pandas as pd
demo_arr=np.array([[1,5,8,8],[2,2,4,9],[7,4,2,3],[3,0,5,2]])
df_obj=pd.DataFrame(demo_arr,columns=['A','B','C','D'])
print(df_obj)
#df_obj=df_obj.sort_values(by=['B'],ascending=True)
#print(df_obj)
#df_obj.to_csv('write_data.csv',index=False)
#print(df_obj)
os.system("pause")