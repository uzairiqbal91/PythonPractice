#!/usr/bin/env python
# coding: utf-8

# # Collection Module
# 

# In[3]:


# default dict
# default dict provides all method that comes from a dictionary but also takes first arguement as a default datatype
# defaultdict never raise a keyerror any key that does not exist get the value return by default factory


# In[4]:


from collections import defaultdict


# In[6]:


# simple dict
d = {'k1' : 1}


# In[7]:


# when use d['k2'] it will throw key error
d['k1']


# In[8]:


d = defaultdict(object)


# In[9]:


# it will not throw an error
d['one']


# In[10]:


# we can also use this by default values use that conjuction using lambda functions

d = defaultdict(lambda : 0)


# In[13]:


# it will reutn 0 when their is not key 
d['one']


# In[14]:


d['two'] = 2


# In[15]:


d


# In[16]:


# it will automatically assign key pair values with default value when try to the key which is not in dict


# In[ ]:




