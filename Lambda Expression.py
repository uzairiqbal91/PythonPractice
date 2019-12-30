#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lambda expression are known as anonymous functions 
# one time use functions
# and never refernccene them again


# In[2]:


def square(num):
    return num**2


# In[3]:


my_nums = [1,2,3,4,5]


# In[13]:


# I wanna do mu_nums valus all to square individually what is the possible soluton?
# loop ? why not map?


# # MAP

# In[5]:


map(square , my_nums)


# In[6]:


for item in map(square , my_nums):
    print(item)


# In[ ]:





# I want the list back 
# list(map(square,my_nums))

# In[10]:


def checkEven(num):
    return num % 2 == 0


# In[11]:


my_nums = [1,2,3,4,5,6,7,8,9,10]

# check numbers that even or odd 


# In[12]:


list(map(checkEven , my_nums))


# # FILTER

# In[17]:


# Differece between filter and map , map iterate all the values but filter filter the condition 
# and get only that list thats meet the filter condition


# In[18]:


list(filter(checkEven , my_nums))


# # Lambda

# In[21]:


# def square_func(num) : return num**2
# replace def to lambda
# arguemtn num and delete the return 
# it is anonymus it has no name
# it uses one time


square = lambda num : num**2
square(10)


# In[33]:


# convert this function to lambda expression
# def checkEven(num):
#     return num % 2 == 0



checkEven = lambda num : num % 2 == 0

checkEven(2)
checkEven(5) 

my_nums = [1,2,3,4,5,6,7,8,9,10]

# check list indivdiual items that either even or odd using map

list(map(checkEven,my_nums))



# In[25]:


# check list indivdiual items that either even or odd using filter


# In[34]:


list(filter(checkEven,my_nums))


# In[ ]:




