#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


dataset = pd.read_csv('Marketing_Data.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, :1]
print(dataset)
print(X)
print(y)


# In[3]:


dataset.isnull().sum()


# In[4]:


dataset.head()


# In[5]:


dataset.tail()


# In[6]:


dataset.describe()


# In[7]:


dataset.info()


# In[8]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)
X_train, X_test, y_train, y_test


# In[9]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[10]:


y_pred = regressor.predict(X_test)
y_pred


# In[13]:


for i in dataset.columns:
    sns.boxplot(dataset[i])
    plt.show()
    


# In[14]:


from sklearn.metrics import r2_score, accuracy_score
r2_score(y_test,y_pred)*100


# In[ ]:




