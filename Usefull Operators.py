#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1,2,3,4]


# In[2]:


# range 
# range is usfeul when we give range to loop using start , final and step size aswell range(start,stop,stepsize)


for num in range(10):
    print(num)


# In[11]:


# loop form 1 to 5
for num in range(0,5):
    print(num)


# In[14]:


# with step size 2
for num in range(0,10,2):
    print(num)


# In[16]:


# making list
m_list=list(range(1,10,2))
m_list


# In[23]:


# suppose we have condition like this 
# we need to print value and index both

my_str = 'uzair'
counter = 0

for item in my_str :
    print(item)
    print(counter)
    counter+=1
    

# in this scenarior we are incrementing counter and iterate to the character of string so best practice is using wrd
#enumerate


# In[20]:


#enumerate


# In[24]:


for item in enumerate(my_str):
    print(item)
    


# In[25]:


for index,item in enumerate(my_str):
    print(item)
    print(index)


# In[28]:


# zip
# zip is opposite to enumerate function

# let

myitem = [0,1,2,3,4]
myitem1 = ['u','z','a','i','r']

for item in zip(myitem,myitem1):
    print(item)


# In[30]:


for item,val in zip(myitem,myitem1):
    print(val)
    print(item)
    


# In[31]:


list(zip(myitem,myitem1))


# In[32]:


# in keyword
# in usefull in loop aswell as in conditional aswell

"uzair" in ["uzair","iqbal"]


# In[33]:


# input 
# input is use when want to get input from the user

result = input('input number')
result


# In[34]:


# other useful operators are
# min , max , randint 


# In[ ]:




