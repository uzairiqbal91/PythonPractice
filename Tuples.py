#!/usr/bin/env python
# coding: utf-8

# # Tuples are versy similar to list . However they have one key difference - immutability once an elemenet is indside in tuple , it can not be reassigned , tuple use parenthesis (1,2,3)

# In[1]:


my_tuple = (1,2,3)


# In[2]:


my_tuple


# In[3]:


type(my_tuple)


# In[4]:


my_list = [1,2,3]


# In[5]:


my_list


# In[6]:


type(my_list)


# In[9]:


# get value index
my_tuple.index(2)


# In[12]:


# count how many time value occured
my_tuple.count(2)


# In[14]:


# check immutabilty 

my_list[1] = 'uzair'
my_list


# In[15]:


# but in tuple it will thorugh an error  "'tuple' object does not support item assignment"

my_tuple[1] = 'uzair'


# In[ ]:




