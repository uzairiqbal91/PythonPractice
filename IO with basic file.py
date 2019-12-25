#!/usr/bin/env python
# coding: utf-8

# In[9]:


# this %% magic is only available in jupyter notebook to write text file


# In[22]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'hello this is a text file\nmy name is uzair')


# In[23]:


# opening file that created above
myfile = open('myfile.txt')


# In[24]:


myfile.read()


# In[25]:


pwd


# In[26]:


# after first time .read function returns empty string because when first time reads than cursor moves to end that is why
myfile.read()


# In[27]:


#  solution -- seek(0) return the cursor to 0 
myfile.seek(0)
myfile.read()


# In[28]:




myfile.seek(0)
myfile.readlines()


# In[ ]:


# open file with file lcoation 
# full file path = 'C:\\User\\ ..' in windows
# full file path = 'User/yourname/ ..' in macOs

# myfile = open('full file path')


# In[30]:


# we should close after reada the file because its opened because it will return error 'this file is using somewhere else'
myfile.close()


# In[31]:


# to avoid previous error in shown in comment best practice to read the file is use special 'with statement'

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


# In[32]:


contents


# In[33]:


# we also use mode read or write 
with open('myfile.txt',mode='r') as my_new_file:
    contents = my_new_file.read()


# In[34]:


contents


# In[36]:


# r = read only
# w = write only
# a = append only
# r+ = is reading and writing
# w+ = is writng and reading overwrite existing file or creates a new file

with open('myfile.txt',mode='w') as my_new_file:
    my_new_file.write('writng the file')


# In[37]:


with open('myfile.txt',mode='r') as my_new_file:
    print(my_new_file.read())


# In[ ]:




