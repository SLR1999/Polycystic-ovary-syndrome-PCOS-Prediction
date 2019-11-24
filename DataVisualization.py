#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[50]:


df = pd.read_csv('data/data without infertility _final.csv')


# In[51]:


#Deleting unwanted columns
del df['Unnamed: 42']
del df['Patient File No.']
del df['Sl. No']
df = df.dropna()
df.drop(df.index[305])


# In[52]:


#Plotting  histogram for outlier detection
#Excluding columns which has binary values
# cols = list(df.columns)

# for col in cols:    
#     if(col.strip()[-5:]) != "(Y/N)":
#         plt.scatter([var for var in range(len(df[col]))], df[col])
#         plt.xlabel('Sr. No.')
#         plt.ylabel(col)
#         plt.show()

#Outliers in the following columns:
#  Pulse Rate(bpm) -
#  Cycle(R/I)
#  FSH(mIU/mL) -
#  LH(mIU/mL) -
#  FSH/LH - 
#  TSH(mIU/L)
#  Vit D3(ng/mL) - 
#  PRG(ng/mL)
#  RBS(mg/dl)
#  BP Systolic - 
#  BP Diastolic -

    
    


# In[69]:


#Plot Correlation Matrix
corr = df.corr()
sns.heatmap(corr,cmap="Blues", center=0, square=True,linewidths=.5)


# In[71]:


#Plotting Correlation Matrix
f = plt.figure(figsize=(19, 15))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=7, rotation=90)
plt.yticks(range(df.shape[1]), df.columns, fontsize=7)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.show()


# In[ ]:




