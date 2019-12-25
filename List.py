#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [1,2,3]
my_list


# In[2]:


my_list[1:]


# In[3]:


my_list[:2]


# In[4]:


#  here is same as string that [1:3] means index 1 till <3 index
my_list[1:3]


# In[5]:


second_list = [4,5,6]


# In[6]:


#  concatination of list 
new_list = my_list+second_list
new_list


# In[7]:


new_list[0] = "uzair"


# In[8]:


# in list we can add any data type 
new_list


# In[9]:


# by appending we can add new value in list 
new_list.append(9)


# In[10]:


new_list


# In[11]:


# by pop we can get last value and delete that value from list of index 
new_list.pop()


# In[20]:


str1 = [4,5,1,2,3,6,6,8]
str2 = ['b','c','a','g','e','i','l','f']


# In[21]:


#  this is sorting function of string but for sorting we have to put all values in one datatype
str1.sort()
str1


# In[22]:


str2.sort()


# In[23]:


str2


# In[24]:


#  this is a reverse function of list 
str1.reverse()


# In[25]:


str1


# In[ ]:




