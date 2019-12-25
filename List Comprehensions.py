#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list comprehensions are a unique way of creating a list in python
# if you fine creating list using .append() in loop 
# than list comprehension is useful for you


# In[2]:


my_list = 'hello'


# In[3]:


mylist = []

for letter in my_list:
    mylist.append(letter)


# In[4]:


mylist


# In[7]:


# best way is list comprehension
mylist = []
mylist = [letter for letter in my_list]


# In[8]:


# same thing
mylist


# In[9]:


myname = [x for x in 'uzair']


# In[10]:


myname


# In[11]:


num_array = [x for x in range(1,10,2)]


# In[12]:


num_array


# In[22]:


# with condition 
# first x is a return value
num_array = [x for x in range(0,10,1) if x % 2 == 0]


# In[18]:


num_array


# In[27]:


# condition in both side
# but without x in first condition not running throw an error
num_array = [x if x<5 else '000' for x in range(0,10,1) if x % 2 == 0]


# In[28]:


num_array


# In[36]:


# nested list comprehensions
# solutuon of nested loop


nested = [x+y for x in [1,10,100] for y in [1,10,100]]


# In[37]:


nested


# In[ ]:




