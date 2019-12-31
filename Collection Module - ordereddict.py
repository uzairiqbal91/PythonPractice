#!/usr/bin/env python
# coding: utf-8

# In[1]:


# simple dict does not retain any order , how you add the keys and values to the dictionary
# well in the ordered dictionary you will retain the order


# In[31]:


d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


# In[32]:


d


# In[33]:


# you can see the output that order is not retain in simple dict
for k,v in d.items():
    print(k,v)


# In[26]:


from collections import OrderedDict


# In[34]:


d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5





# In[35]:


for k,v in d.items():
    print(k,v)


# In[36]:


d1 = {}
d1['a'] = 1
d1['b'] = 2


# In[37]:


d2 = {}
d2['b'] = 2
d2['a'] = 1


# In[38]:


print (d1 == d2)


# In[39]:


d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2


# In[40]:


d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


# In[41]:


print (d1 == d2)


# In[ ]:


# see that in normal dict it return false but in ordered dict it return true because of order

