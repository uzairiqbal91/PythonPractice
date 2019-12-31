#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[4]:


# hour , minute , second , microsecond
t = datetime.time(14,5,5)


# In[8]:


print(t)


# In[10]:


# you can get minute hour and seconds individually
t.minute


# In[11]:


print(datetime.time.min)


# In[12]:


print(datetime.time.max)


# In[18]:


# for getting todays date

today = datetime.date.today()
print(today)


# In[19]:


today.timetuple()


# In[20]:


today.month


# In[21]:


today.day


# In[22]:


d1 = datetime.date(2019,12,31)


# In[24]:


print(d1)


# In[25]:


d2 = d1.replace(year = 2020)


# In[26]:


print(d2)


# In[ ]:




