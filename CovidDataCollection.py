#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd


# In[7]:


df1=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data1.csv')
df2=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data2.csv')
df3=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data3.csv')
df4=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data4.csv')
df5=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data5.csv')
df6=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data6.csv')
df7=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data7.csv')
df8=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data8.csv')
df9=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data9.csv')
df10=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data10.csv')
df11=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data11.csv')
df12=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data12.csv')
df13=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data13.csv')
df14=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data14.csv')
df15=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data15.csv')
df16=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data16.csv')
df17=pd.read_csv('https://api.covid19india.org/csv/latest/raw_data17.csv')


# In[11]:


df17


# In[13]:


df17.info()


# In[17]:


df1.columns


# In[48]:


df2.columns


# In[52]:


df1=df1.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df2=df2.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df3=df3.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df4=df4.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df5=df5.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df6=df6.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df7=df7.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df8=df8.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df9=df9.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df10=df10.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df11=df11.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df12=df12.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df13=df13.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df14=df14.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df15=df15.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df16=df16.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]
df17=df17.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State','Current Status']]


# In[ ]:





# In[54]:


df=df1.append([df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17])
df


# In[ ]:





# In[62]:


DATE=df['Date Announced'].str.split('/',expand=True)
DATE.columns=['Day','Month','Year']
DATE


# In[63]:


df


# In[65]:


pwd


# In[66]:


data=pd.read_csv('C:\\Users\\Subhajit\\Covid19Ind.csv')
data

