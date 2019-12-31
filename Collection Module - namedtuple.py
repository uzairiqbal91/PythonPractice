#!/usr/bin/env python
# coding: utf-8

# In[1]:


# named tuple can assign names as well as numerical index 
# in the normal tuple you can not assign name


# In[2]:


t = (1,2,3)


# In[3]:


t[0]


# In[4]:


from collections import namedtuple


# In[8]:


# you have to assign type name and field name like class 
Dog = namedtuple('Dog','age breed name')

# now age , breed and name is a constructor of a class Dog
# its a fast method to create class


# In[7]:


sam = Dog(age=2 , breed = 'lab' , name = 'Sammy')


# In[12]:


sam


# In[13]:


sam.age


# In[20]:


# u can get by index aswell like in tupple
sam[0] #referes to age


# In[32]:


# you have to name the variable same as class name otherwise it will not work

Cat = namedtuple('Cat','fur claws name')


# In[35]:


c = Cat(fur = 'a' , claws = 'b' , name = 'c')


# In[37]:


c[0]


# In[38]:


c.fur


# In[ ]:





# In[ ]:




