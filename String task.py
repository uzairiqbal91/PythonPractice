#!/usr/bin/env python
# coding: utf-8

# indexing and sliing of String 
# 

# In[1]:


myString = 'Hello World'


# In[2]:


myString[1]


# In[3]:


myString[3]


# In[4]:


#last letter 
myString[-1]


# Now Slicing

# In[5]:


myString = 'abcdefghk'


# In[6]:


myString[2]


# In[7]:


myString[2:]


# In[8]:


myString[:3]


# # start point include in string but final point doesnt
# myString[3:6]

# In[10]:


myString[1:3]


# Now Use Step Size
# [start:final:step]

# In[16]:


#that means parse the string but jump to 2 means step size 2
# a->b->c print c after a -> means step size
myString[::2]


# In[17]:


myString[::3]


# # all combining example

# In[19]:


# 1 start index that is b includes as I mentioned above , 6 is final point that is 'g' but g not includes so our string will be b,c,d,e,f
# b,c,d,e,f
# now that string will parse with step size b->c->d = bd that d->e->f the answer will be bdf   
myString[1:6:2]


# for reverse string

# In[21]:


# parse string reversely
myString[::-1]


# In[ ]:




