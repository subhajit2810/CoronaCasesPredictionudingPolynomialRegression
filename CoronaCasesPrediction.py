#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


data=pd.read_csv('C:\\Users\\Subhajit\\Covid19Ind.csv')
data


# In[5]:


Day=data[data['Current Status']=='Hospitalized'].groupby(['Month','Day'])['Num Cases'].sum()
Day


# In[6]:


x=np.arange(len(Day))
x


# In[7]:


y=Day.values
y


# In[39]:


from sklearn.preprocessing import PolynomialFeatures
Poly=PolynomialFeatures(degree=5)
X=Poly.fit_transform(x.reshape(-1,1))
X


# In[40]:


pd.DataFrame(X)


# In[41]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X,y)


# In[42]:


reg.coef_


# In[43]:


reg.intercept_


# In[44]:


Yp=reg.predict(X)
Yp


# In[45]:


plt.scatter(x,y)
plt.plot(x,Yp,color='k')
plt.show()


# In[32]:


reg.score(X,y)*100


# In[33]:


x


# In[46]:


reg.predict(Poly.transform([[235]]))


# In[ ]:




