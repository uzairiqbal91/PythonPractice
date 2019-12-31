#!/usr/bin/env python
# coding: utf-8

# In[1]:


# time it is used for timing your code to cehcking complexity of your code


# In[2]:


import timeit


# In[3]:


'0-1-2-3-4-5-.....-99'


# In[10]:


# first arguemtn is your code put in string and second is how many time you want to run

timeit.timeit('"-".join(str(n) for n in range(100))',number=1000)


# In[11]:


# its is faster than previous code

timeit.timeit('"-".join([str(n) for n in range(100)])',number=1000)


# In[14]:


# now you can see map is much faster than previous two , may be because it is not putting loop

timeit.timeit('"-".join(map(str,range(100)))',number=1000)


# In[17]:


# magic % by timint generate the individual time of loop
get_ipython().run_line_magic('timeit', '"-".join(str(n) for n in range(100))')


# In[18]:


get_ipython().run_line_magic('timeit', '"-".join([str(n) for n in range(100)])')


# In[19]:


get_ipython().run_line_magic('timeit', '"-".join(map(str,range(100)))')


# In[ ]:


# you can see that map is mush faster than simple and list comprehension

