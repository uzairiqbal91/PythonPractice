#!/usr/bin/env python
# coding: utf-8

# + and * properties of String

# In[1]:


myString = 'Hello World'


# + is concatination

# In[4]:


# Concatincation example
myString + " this is UZAIR"


# In[6]:


# you will see that above concatination saved because string concatination is myString = MyString + 'anything'
myString = myString + ' this is Uzair'
print(myString)


# In[9]:


#2+3 = 5 in number variable 
#but in '2' + '3' is '23' that is String concatination
'2' + '3'


# In[11]:


a = '3'
print(a)


# In[14]:


# * is a property of string that means * of string concatination with that time of numbers
# a*3 = a+a+a
print(a*5)


# String methods

# In[26]:


# To get String methods put . after string and tap tab key to get all methods
a = 'a b c'
a.capitalize()


# In[27]:


a.upper()


# In[29]:


# by default split with space character
a.split()


# In[31]:


a = 'aibic'
# split with i chracter
a.split('i')


# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)

# # Formatting with .format() method
# good way to format object into your string for print statement
# {} statement in print and .format put into that {} statement

# In[33]:


print('This is a string {}'.format('This is uzair'))


# In[34]:


print('The {} {} {}'.format('fox','brown','quick'))


# In[35]:


# {1} means .format(0->'',1->'',2->'')
print('The {1} {0} {2}'.format('fox','brown','quick'))


# In[36]:


# we can also assign variable into .format() method and refere to that variable in print()


# In[40]:


print('The {a} {b} {c}'.format(a='Muhammad',b='Uzair',c='Iqbal'))


# In[42]:


print('The {a} {a} {a}'.format(a='Muhammad',b='Uzair',c='Iqbal'))


# # Float formatting follows "{value:width.precision f}"

# In[47]:


result = 100/777


# In[48]:


print(result)


# In[55]:


# for correct precission below is the example using format() method
print('The result is {r:.3f}'.format(r = result))


# In[56]:


result = 104.12345


# In[57]:


print('The result is {r:.3f}'.format(r = result))


# String injection in print with f before print method

# In[62]:


f_name = 'Muhammad'
m_name = 'Uzair'
l_name = 'Iqbal'


# In[63]:


print(f'my full name is {f_name} {m_name} {l_name}')


# In[64]:


print('I like {}'.format('apples'))


# In[ ]:





# In[ ]:




