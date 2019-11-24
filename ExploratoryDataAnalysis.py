#!/usr/bin/env python
# coding: utf-8

# In[188]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[189]:


df = pd.read_csv("data/data without infertility _final.csv")

del df["Unnamed: 42"]
del df['Sl. No']
del df['Patient File No.']

null_columns=df.columns[df.isnull().any()]
df[null_columns].isnull().sum()


# In[190]:


# print(df[df.isnull().any(axis=1)][null_columns])


# In[191]:


df = df.dropna()
df.drop(df.index[305])
# print(max(df['AMH(ng/mL)']))


# In[192]:


# print(df[df.isnull().any(axis=1)][null_columns])


# In[199]:


# del df['AMH(ng/mL)']
l = df.columns.values

number_of_columns = 10
number_of_rows = len(l)-1/number_of_columns
plt.figure(figsize=(2*number_of_columns,10*number_of_rows))
for i in range(0,len(l)):
    plt.subplot(number_of_rows + 1,number_of_columns,i+1)
    sns.set_style('whitegrid')
    sns.boxplot(df[l[i]],color='blue',orient='v')
    plt.tight_layout()
    


# In[194]:


fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(df)


# In[ ]:




