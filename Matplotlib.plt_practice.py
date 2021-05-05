#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


from matplotlib import pyplot as plt
plt.plot([1,2,3], [4,5,1])
plt.show()


# In[3]:


from matplotlib import pyplot as plt
x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)
plt.title('Info')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.show()


# In[6]:


from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y, 'g',label='lineone',linewidth=5)
plt.plot(x2,y2, 'c',label='linetwo',linewidth=5)
plt.title('Epic info')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True, color = 'k')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9], [5,2,7,8,2], label='Exampleone', color = 'r')
plt.bar([2,4,6,8,10], [8,6,2,5,6], label= 'ExampleTwo', color = 'g')
plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Info')
plt.show()


# In[10]:


import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()
        


# In[11]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
          


# In[13]:


import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[], color = 'm', label= 'sleeping', linewidth=5)
plt.plot([],[], color = 'c', label= 'Eating', linewidth=5)
plt.plot([],[], color = 'r', label= 'Working', linewidth=5)
plt.plot([],[], color = 'k', label= 'playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('stackplt')
plt.legend()
plt.show()


# In[15]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping', 'eating','working','playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels= activities,
        colors= cols,
        startangle= 90,
        shadow= True,
        explode= (0, 0.1,0,0),
        autopct= '%1.1f%%')

plt.title('pieplot')
plt.show()


# In[16]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activites = ['sleeping', 'eating', 'working','playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels = activites,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0, 0.1,0,0),
        autopct = '%1.1f%%')
plt.title('pieplot')
plt.show()


# In[1]:


import matplotlib.pyplot as plt


# In[2]:


from matplotlib import pyplot as plt
plt.plot([1,2,3,4], [5,6,7,8])
plt.show()


# In[3]:


from matplotlib import pyplot as plt
x = [5,8,10]
y = [12,16,6]
plt.plot(x,y)
plt.title('Info')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[4]:


from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x2,y2,'c',label='linetwo',linewidth=5)
plt.title('Epicinfo')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True, color='k')
plt.show()


# In[5]:


import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2], label = 'Example one')
plt.bar([2,4,6,8,10], [8,6,2,5,6], label='Example two')
plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Info')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Histogram')
plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter plot')
plt.legend()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating', 'working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0,0.1,0),
        autopct = '%1.1f%%')

plt.title('pieplot')
plt.show()


# In[12]:


import matplotlib.pyplot as plt
plt.bar(['Java', 'Python', 'PHP', 'JavaScript', 'C#'], [22.2, 17.6, 8.8, 8, 7.7])
plt.title('Bar graph')
plt.xlabel('Programming languages')
plt.ylabel('Popularity')
plt.legend()
plt.show()
         
         


# In[17]:


#Write a Python programming to display a horizontal bar chart of the popularity of programming Languages. Go to the editor
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
#The code snippet gives the output shown in the following screenshot



import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color = 'g')
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
plt.show()


# In[22]:


#Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.


import matplotlib.pyplot as plt 

x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x, popularity, color = ['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.show()
           


# In[25]:


#Write a Python programming to display a bar chart of the popularity of programming Languages. Attach a text label above each bar displaying its popularity (float value)

import matplotlib.pyplot as plt


x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x, popularity, color = ['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xlabel('Popularity')
plt.ylabel('Languages')
for index, value in enumerate(popularity):
    plt.text(value, index, str(value))
plt.show()


# In[2]:


from matplotlib  import pyplot as plt
plt.plot([1,2,3], [4,5,1])
plt.show()


# In[3]:


from matplotlib import pyplot as plt
x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)
plt.title('Info')
plt.xlabel('x axis')
plt.ylabel("y axis")
plt.show()


# In[5]:


from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g', label='line one', linewidth=5)
plt.plot(x2,y2,'c', label= 'line two', linewidth=5 )
plt.title("Epic info")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True, color = 'k')
plt.show()


# In[6]:


import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9], [5,2,7,8,2], label = 'Example one')
plt.bar([2,4,6,8,10], [8,6,2,5,6], label = 'Example two')
plt.title('Info')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("Histogram")
plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label = 'skitscat', color='k', s= 25, marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter plot')
plt.legend()
plt.show()


# In[13]:


import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'])
plt.plot([],[], color='m', label='sleeping', linewidth=5)
plt.plot([],[], color='c', label='Eating', linewidth=5)
plt.plot([],[], color='r', label= 'Working',linewidth=5)
plt.plot([],[], color='k', label='playing',linewidth=5)

plt.title('stck plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[17]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating', 'working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0,0.1,0),
        autopct = '%1.1f%%')

plt.title('pieplot')
plt.show()
        
        


# In[22]:


import matplotlib.pyplot as plt

Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
Programming_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', ' C++'] 

cols = ['c','m','r','b']

plt.pie(Popularity,
        labels = Programming_languages,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0.1,0,0,0,0),
        autopct = '%1.1f%%')

plt.title('pieplot')
plt.show()
        


# In[1]:


from matplotlib import pyplot as plt
plt.plot([1,2,3], [4,5,1])
plt.show()


# In[4]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x = [5,8,10]
y = [12,16,1]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x2,y2,'c',label='linetwo',linewidth=5)
plt.title('EpicInfo')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.grid(True, color = 'k')
plt.show()


# In[5]:


import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9], [5,2,7,8,2], label = 'Exampleone')
plt.bar([2,4,6,8,10], [8,6,2,5,6], label = 'Exampletwo', color ='g')
plt.legend()
plt.xlabel('Bar number')
plt.ylabel('Bar height')
plt.title('Info')
plt.show()


# In[6]:


import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.title('Histogram')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='k',s=25,marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k',s=25,marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[11]:


import matplotlib.pyplot as plt


days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m', label='sleeping',linewidth=5)
plt.plot([],[],color='c', label='Eating',linewidth=5)
plt.plot([],[],color='r', label='Working',linewidth=5)
plt.plot([],[],color='k', label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing, colors = ['m','c','r','k'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[12]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping', 'eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        explode= (0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('pieplot')
plt.show()


# In[22]:


import matplotlib.pyplot as plt
Popularity = [22.2, 17.6, 8.8, 8]
Programming_languages =['Java', 'Python', 'PHP', 'JavaScript']
cols = ['m', 'k', 'r', 'k']


plt.pie(Popularity,
         labels = Programming_languages,
         colors = cols,
         startangle = 90,
         explode = (0,0.1,0,0),
         shadow = True,
         autopct = '%1.f%%')
plt.title('pieplot')
plt.show()


# In[2]:


from matplotlib import pyplot as plt
plt.plot([1,2,3,4], [5,6,7,8])
plt.show()


# In[6]:


from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g', label='lineone', linewidth=5)
plt.plot(x2,y2,'c', label='lineone', linewidth=5)
plt.title('Info')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[7]:


import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9], [5,2,7,8,2], label ='Exampleone')
plt.bar([2,4,6,8,10], [8,6,2,5,6], label='Exampletwo')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Info')
plt.show()


# In[8]:


import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.title('Histogram')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s= 25, marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[], color='m', label= 'sleeping', linewidth=5)
plt.plot([],[], color='c', label= 'eating', linewidth=5)
plt.plot([],[], color='r', label=  'working', linewidth=5)
plt.plot([],[], color='k', label= 'playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('stck plot')
plt.legend()
plt.show()


# In[1]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping', 'eating','working','playing']
cols = ['m', 'c', 'r', 'b']

plt.pie(slices,
        labels = activities,
        colors = cols,
        shadow = True,
        startangle = 90,
        autopct = '%1.1f%%',
        explode = (0,0.1,0,0))

plt.title('pie plot')


# In[2]:


from matplotlib import pyplot as plt
plt.plot([2,3,4], [5,6,7])
plt.show()


# In[3]:


from matplotlib import pyplot as plt
x = [3,4,5,6]
y = [1,3,6,7]

plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Info')
plt.show()


# In[4]:


from matplotlib import pyplot as plt
from matplotlib import style
 
style.use('ggplot')

x = [3,4,5,6,7]
y = [1,2,3,4,5]

x2 = [5,6,7,8,9]
y2 = [1,3,5,7,11]

plt.plot(x,y, 'g', label = 'lineone', linewidth=5)
plt.plot(x2,y2, 'g',label = 'linetwo', linewidth=5)
plt.title('Info')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[5]:


import matplotlib.pyplot as plt

plt.bar([2,3,4,5,6], [4,5,6,7,8], label = 'Exampleone', color = 'g')
plt.bar([3,5,7,9,10], [1,3,5,2,4], label = 'Exampletwo', color = 'r')
plt.title('Bar graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[6]:


import matplotlib.pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.title('Histogram')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


# In[7]:


import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y = [3,4,5,6,7,8]

plt.scatter(x,y, label='skitscat', color='k', s= 25, marker='o')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[8]:


import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[], color='m', label= 'sleeping', linewidth=5)
plt.plot([],[], color='c', label= 'eating', linewidth=5)
plt.plot([],[], color='r', label=  'working', linewidth=5)
plt.plot([],[], color='k', label= 'playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('stck plot')
plt.legend()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activites = ['sleeping', 'working', 'playing', 'eating']
cols = ['m', 'r', 'g', 'b']

plt.pie(slices,
        labels = activites,
        colors = cols,
        startangle = 90,
        autopct = '%1.1f%%',
        explode = (0,0.1,0,0),
        shadow = True)

plt.title('pie chat')
plt.show()


# In[ ]:




