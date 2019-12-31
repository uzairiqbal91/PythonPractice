#!/usr/bin/env python
# coding: utf-8

# In[1]:


# generator functin allows us to write a function that can send back a 
# value and then later resume to pick up where it left off


# In[2]:


# squence of values over time


# In[3]:


# yield statemtn is a difference in generator


# In[5]:


# when a generaotr function in compiled they become an object that supports an iteration protocol
# that meand when they are called in your code they dont actually return a value and then exit


# In[6]:


# they automatically suspend and resume tehir execution and state around a last point of value generation
# the advantage is that istead of having to compute an entire series of value up front , the generator computes one value 
# waits until the next value is called for


# In[7]:


def create_cubes(n):
    
    result = []
    for x in range(n):
        result.append(x**3)
    return result    


# In[8]:


create_cubes(10)


# In[9]:


# save a list of number takes a lot of memory and print individually we have to take another loop

for x in create_cubes(10):
    print(x)


# In[18]:


# save a list of number takes a lot of memory and print individually we have to take another loop better way to yield 

def create_cubes(n):
    
    
    for x in range(n):
        yield x**3
    


# In[33]:


list(create_cubes(10))


# In[34]:


# instead of taking loop use next 
# for x in create_cubes(10):
#     print(x)


# In[35]:


g = create_cubes(10)


# In[36]:


# it eill reutn next number of the previous one 

next(g)


# In[37]:


next(g)


# In[39]:


# suppose taking simple string 

string = "Uzair"


# In[47]:


# next(string) throw an error because next only use when yield called so for the next item without yield
# we use iter , iter turn the string to generator

# next(string)
my_str=iter(string)


# In[48]:


# now you can call next in string because it converted in generator
next(my_str)


# In[49]:


next(my_str)


# In[ ]:




