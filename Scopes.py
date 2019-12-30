#!/usr/bin/env python
# coding: utf-8

# In[23]:


number = 50


# In[24]:


def myFun():
    global number
    number = 100 
    print(number)

# here number is a global number but i want to change in my function how can i change in python 
# because by this we can not change the global value


# In[25]:


myFun()


# In[26]:


number


# In[ ]:




