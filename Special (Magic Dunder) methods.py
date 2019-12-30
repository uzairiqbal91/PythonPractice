#!/usr/bin/env python
# coding: utf-8

# In[19]:


# special or dunder methods use double underscore ' __ ' , example __init__ mehtods this is a magic method

class Books():
    
    def __init__(self,title,pages):
        self.pages = pages
        self.title = title
    
#   this is a magic method
    def __str__(self):
        return f"{self.title} by {self.pages}"
    
    
    def __len__(self):
        return self.pages
    
    
    def __del__(self):
        print("objec has been deleted")
        


# In[20]:


book = Books("harry potter",10)


# In[21]:


# when I print the book that it give some representation what if I need the string ? answer is by using magic/dunder method
# __str__(self)

print(book)


# In[22]:


# same wit len , we use __len__(self) magic method

len(book)


# In[23]:


del(book)


# In[ ]:




