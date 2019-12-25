#!/usr/bin/env python
# coding: utf-8

# # Difference between List and Dictionaries
# # dictionaries are used as unordered and get value by its key name while list retrived by location (index) and used when order required , Dictionaries can not be sorted because of key value pair

# In[24]:


my_dict = {'key1':'a','key2':2,'key3':3,'key4':4,'key5':5}


# In[25]:


type(my_dict)


# In[26]:


#  get value by its key name
my_dict['key1']


# In[27]:


# nested dictionaries 

dict1 = {
    'data':
    {
    
    
    'info':{
    'name' : 'uzair',
    'age' : 26
    },
    'address' :{
    'street' : 'gulshan',
    'city' : 'karachi',
    'country' : 'pakistan'
    
    }
        }
    }


# In[28]:


dict1['data']['info']['name']


# In[29]:


dict1['data']['address']['city']


# In[30]:


# changing value 
dict1['data']['address']['city'] = 'Lahore'


# In[31]:


dict1['data']['address']['city']


# In[34]:


dict1.values()


# In[35]:


dict1.keys()


# In[36]:


dict1.items()


# In[ ]:




