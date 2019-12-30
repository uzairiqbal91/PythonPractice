#!/usr/bin/env python
# coding: utf-8

# In[1]:


# function witout arguement and return void
def my_fun():
    print("hello world")


my_fun()

# function with arguement and return void
def my_func_withparam(name):
    print(name)
    
my_func_withparam("uzair")

def my_func_withparam_default(name = "UZAIR"):
    print(name)
    
my_func_withparam_default()

my_name = my_func_withparam("Uzair")
print(type(my_name))
# it will return NoneType so the reutrn type of my_name is Void



# function with arguement and return Int
def add_two_number(num1,num2):
    return num1+num2
    

addVal = add_two_number(2,4)

print(type(addVal))
# it will return Int so the reutrn type of addVal is Int


# In[ ]:




