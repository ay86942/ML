#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,0:1].values
y = dataset.iloc[:,1:2].values
print(dataset)
print(X)
print(y)


# In[5]:


dataset.isnull().sum()


# In[6]:


dataset.head()


# In[7]:


dataset.tail()


# In[8]:


dataset.describe()


# In[9]:


dataset.info()


# In[10]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train, X_test, y_train, y_test


# In[11]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[12]:


y_predict = regressor.predict(X_test)
y_predict


# In[14]:


plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[15]:


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[16]:


regressor.score(X_test,y_test)*100


# In[18]:


from sklearn.metrics import r2_score
r2_score(y_test,y_predict)*100


# In[ ]:




