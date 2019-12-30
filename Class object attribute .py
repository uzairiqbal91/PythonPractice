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


# In[60]:


# __init function call whenever create the instance its like a constructor
# self keyword is use for that this function is belong to the current class like getting context of a class or its a reference of the class

class Dog():
    
#     Class object attribure
#     Same in any instance of a class
#     no need self keyword because self is a reference of a specific instance

    species = 'Mammal'
    
    def __init__(self,bread,name,age,isGerman):
        
#         assign it using self.attribute name
#           you can take any of name in paramater like bread1 and self.bread = bread1 it will work!
        self.bread = bread
        self.name = name
        self.age = str (age) + " months"
        self.isGerman = isGerman
        
# Operations / Actions -> Methods
# eg in case of Dog is bark()
        
    def bark(self):
        print('Wooof ! my name is {}'.format(self.name))




# In[ ]:





# In[61]:


# here is making instance of Class Dog and you can get by attribute by ' . '
my_dog = Dog("bread","tommy",6,False)


# In[62]:


my_dog.species


# In[63]:


my_dog.bark()


# In[ ]:





# In[64]:


# example with default value of an attribute

class Circle():
    
    pi_val = 3.14
    
    def __init__(self,radius = 1):
        self.radius = radius
        


# In[65]:


# when you using default value of an attribute than not necessory to give attribute val while making instance

circle = Circle()


# In[66]:


circle.radius


# In[ ]:




