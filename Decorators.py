#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imagine you create simple function


# In[3]:


# def simple_function():
#     do simple function
#     return something


# In[4]:


# now you created a simple function noy you want to add more functonality to it
# solution is (Simple)

# def simple_function():
#     more code
#     do simple function
#     return something

# now you have two options 
# 1) add more code to older funtion
# 2) create new function that contains older code and add new code

# its not ideeal to copy pase to other function

# but what if you need to remove extra functionally and get back again to older function 
# how can achieve this somw switch on/off ?


# In[5]:


# python has decorators who allows us to take extra functionality to an already existing function
# they use @ operator and are then placed on tp of the origional function


# In[20]:


def hello():
    return 'Hello !'


# In[21]:


hello()


# In[22]:


greet = hello


# In[23]:


greet()


# In[24]:


# when you will delete hello than can no execute hello now
del hello


# In[25]:


hello()


# In[28]:


# but greet still return hello because greet reference the hello 

greet()


# In[35]:


def hello():
    print("hello () function called")
    
    def greet():
        return 'greet'
    
    def welcome():
        return 'welocme'
    
    print(greet())
    print(welcome())
    
    print('This is the end of the function')
    
    


# In[36]:


hello()


# In[37]:


def hello(name = 'Uzair'):
    print("hello () function called")
    
    def greet():
        return 'greet'
    
    def welcome():
        return 'welocme'
    
    if name == 'Uzair':
        return greet()
    else:
        return welcome()
    
    
    print('This is the end of the function')


# In[38]:


hello()


# In[39]:


# what is the good way ?
# make some function and pass to an another function

def hello():
    print("hello")


# In[40]:


def other(some_func):
    print("other code run")
    print(some_func())


# In[43]:


other(hello)


# In[73]:


# we use decorators for it to put extra functionality of function to other function

def new_decorator (originonal_function):
    
    def wrap_func():
        
        print("some extra code before the original function")
        
        originonal_function()
        
        print("some extra code after the original function")
    
    return wrap_func
        

def hello_world(originonal_function):
    print("hello world")
            
    return originonal_function


# In[74]:


# calling decorator function to another function
@hello_world
@new_decorator
def function_need_decorator():
    
    print("I want to be decorated")

function_need_decorator()


# In[75]:


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# In[85]:


@uppercase_decorator
def my_name():
    return "uzair"


# In[86]:


my_name()


# In[92]:



def splitting(function):
    
    def wrapper():
        return function().split()
    
    return wrapper
        


# In[93]:


@splitting
@uppercase_decorator
def my_name():
    return "uzair"


# In[94]:


my_name()


# In[95]:


# Arguments in Decorator Functions

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")


# In[ ]:




