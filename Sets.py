#!/usr/bin/env python
# coding: utf-8

# # Sets are unordered collection of unique elements , meaning there is only one representation of unique element 

# In[1]:


my_set = set()


# In[2]:


my_set


# In[3]:


my_set.add(1)


# In[4]:


my_set.add(2)
my_set.add(3)
my_set


# In[5]:


my_set.add(3)
my_set.add(3)
my_set.add(3)


# In[8]:


# only one representaton of unique item 
my_set


# In[9]:


# we can also convert list to set

my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,6,6,6,7,7,8]


# In[13]:


# this will return uqinue items
set(my_list)


# In[ ]:




