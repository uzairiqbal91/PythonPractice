#!/usr/bin/env python
# coding: utf-8

# In[1]:


# class keyword to make classes and starts with capital for chosing class name

class Sample():
    pass


# In[2]:


sample = Sample()


# In[3]:


type(sample)
# we can see that this sample instance is a Sample type


# In[36]:


# __init function call whenever create the instance its like a constructor
# self keyword is use for that this function is belong to the current class like getting context of a class or its a reference of the class

class Dog():
    
    def __init__(self,bread,name,age,isGerman):
        
#         assign it using self.attribute name
#           you can take any of name in paramater like bread1 and self.bread = bread1 it will work!
        self.bread = bread
        self.name = name
        self.age = str (age) + " months"
        self.isGerman = isGerman
        


# In[37]:


# it gives an error because the constructor takes 1 arguement that is bread
my_dog = Dog()


# In[38]:


# here is making instance of Class Dog and you can get by attribute by ' . '
my_dog = Dog("bread","tommy",6,False)


# In[39]:


my_dog.bread


# In[40]:


my_dog.isGerman


# In[41]:


my_dog.age


# In[ ]:




