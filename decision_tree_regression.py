#!/usr/bin/env python
# coding: utf-8

# # Decision Tree Regression

# ## Importing the libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ## Importing the dataset

# In[2]:


dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
dataset


# ## Training the Decision Tree Regression model on the whole dataset

# In[3]:


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)


# In[4]:


y_pred = regressor.predict(X)


# ## Predicting a new result

# In[11]:


regressor.predict([[6.2]])


# ## Visualising the Decision Tree Regression results (higher resolution)

# In[6]:


X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# In[7]:


regressor.score(X,y)*100


# In[8]:


from sklearn.metrics import r2_score, accuracy_score
r2_score(y,y_pred)*100


# In[9]:


accuracy_score(y_pred,y)*100


# In[ ]:




