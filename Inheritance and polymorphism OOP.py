#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


# # Inheritence

# In[6]:


# Dog is inhereting the Animal class and Dog class than can call the functions and attribute except private

class Dog(Animal):
    
    def __init__(self):
        print("Dog created")
        Animal.__init__(self)
        
    def bark(self):
        print("wofff !")
        
#     ovverriting the method 

    def eat(self):
        print("I am a dog and eating")


# In[7]:


myDog = Dog()


# In[8]:


# you can see that Dog can call the animal functions because of inheritence

myDog.eat()


# In[9]:


myDog.bark()


# # Polmorphism

# In[17]:


# Difference object classes can share the same method name
# those method can be called form same place even though a variety of different object
# example

class Cat():
    
    def __init__(self,name):
        print("Cat created")
        self.name = name
    
    def speak(self):
        return self.name + " Says meoww !"
        


# In[18]:


class Dog():
    
    def __init__(self,name):
        print("Dog created")
        self.name = name
    
    def speak(self):
        return self.name + " Says Woff !"


# In[19]:


dog = Dog("Tommy")


# In[20]:


cat = Cat("catty")


# In[21]:


dog.speak()


# In[22]:


cat.speak()


# In[26]:


# both animal have speak method so create base class Animal and put this method on that class and override to any instance

class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")
        
#     this is an abstract method    
    def speak(self):
        
        raise NotImplementedError("sub class must implment this")


# In[24]:


dog = Dog("Tommy")


# In[25]:


dog.speak()


# In[27]:


animal = Animal()


# In[29]:


# it will return error 
animal.speak()


# In[31]:


# than inherit the Animal class 
class Cat(Animal):
    
    def __init__(self,name):
        print("Cat created")
        self.name = name
    
    def speak(self):
        return self.name + " Says meoww !"


# In[32]:


class Dog(Animal):
    
    def __init__(self,name):
        print("Dog created")
        self.name = name
    
    def speak(self):
        return self.name + " Says Woff !"


# In[34]:


dog = Dog("Tommy")
dog.speak()


# In[35]:


cat = Cat("catty")
cat.speak()


# In[ ]:




