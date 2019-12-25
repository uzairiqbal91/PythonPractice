#!/usr/bin/env python
# coding: utf-8

# In[1]:


# while some_condition:
#     do somthing
#   else:
#       do something


# In[4]:


x = 0 
while x<5 : 
    print(x)
#     x += 1
    x = x + 1 
else:
    print('x is not less than 5')


# # break , continue , pass 

# In[6]:


x = [1,2,3,4]

# it gives an error because python need somthing in loop the solution is pass
# for item in x :
#     # do something


# In[9]:


# pass means hey I am not gonna do anything 

for item in x :
    pass

print('end script')


# In[13]:


# continue means return towards loop condition again 

str1 = 'uzair'

for ch in str1 :
    if(ch == 'a'):
        continue
    else:
        print(ch)


# In[15]:


# break means end the loop 
str1 = 'uzair'

for ch in str1 :
    if(ch == 'a'):
        break
    else:
        print(ch)


# In[ ]:




