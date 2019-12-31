#!/usr/bin/env python
# coding: utf-8

# # Collection Module

# In[3]:


# counter

# it is a dictionary subclass that caount hashable objects

from collections import Counter


# In[4]:


l = [1,2,3,1,1,1,1,111,22,33]


# In[5]:


Counter(l)


# In[6]:


# it counts how many occourence of individual number and reuturn in dictionary

s = "aaaasssdasdsaddddwqeqweqwe"

Counter(s)


# In[11]:


sentence = "How many times does each word show up in the sentence word"


# In[16]:


words = sentence.split()
counter = Counter(words)


# In[18]:


# by using this you can put any natural language processing techniques

sum(counter.values())


# In[ ]:




