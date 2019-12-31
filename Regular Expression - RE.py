#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Regular expression is used for finding text , finding repition etc
# many problems can be solved using regular expression


# In[3]:


import re


# In[4]:


# searching patterns in text


# In[5]:


patterns = ['term1' , 'term2']


# In[6]:


text = 'this is a string with term1 , but not the other term'


# In[7]:


# now how can we use regular expression to search pattern ?


# In[12]:


# first arguemtn is a perticular patterns and other is string
if(re.search('hello','hello world')):
    print('found')
else:
    print('not found')


# In[13]:


if(re.search('hi','hello world')):
    print('found')
else:
    print('not found')


# In[17]:


# likewise in our problem

for item in patterns:
    
    print('searching ' + item)
    
    if(re.search(item , text)):
        print(item + " is found")
    else:
        print(item + " is not found")
    


# In[18]:


match = re.search('hello','hello world')


# In[20]:


match.start()


# In[22]:


match.end()


# In[23]:


# splitting with match string 

split_term = '@'
phrase = 'what is you email , is is uzairiqbal91@gmail.com'


# In[24]:


re.split(split_term,phrase)


# In[25]:


# it becomes two string first before the pattern @ and the other after that


# In[26]:


# split function split with space by default


# In[28]:


'hello world'.split()


# In[39]:





# finding with match string by using regular expression it will return the matched list

match = re.findall('hello','hello wold,hello, hi hello')
len(match)


# In[69]:


# multi re find 

def multi_re_find(patterns,phrase):
    
    for pattern in patterns:
        
        print('searching the phrase using the re check'  + pattern)
        print(re.findall(pattern,phrase))
        print('\n')
        
        

test_phrase = 'sdsd..sssddd..sdddsddd...dsds....dsssss....sdddd'
test_pattern = ['[sd]' ,  # either s or d
                's[sd]+'] # s followed by one or more s or d
                          # + is a character set


# In[70]:


multi_re_find(test_pattern,test_phrase)


# In[71]:


# exclusion

# we can use ^ to exclude terms by incorporating it into the bracket syntax notation
# for example [^...] will match any single character not in bracket  + check the match appears atleast one 


# In[72]:


# '[^!.? ]+' that are not a !,? and space ,

test_phrase = "this is a string! but it has punctuatuions . how can I remove ?"
re.findall('[^!.? ]+',test_phrase)


# In[73]:


# cahracter ranger uses ' - ' 
# example [a-z]


# In[76]:


test_phrase = 'This is an example sentence let see if we can find some letters'

test_patterns = ['[a-z]+'  , # sequence of lower case letter
                '[A-Z]+'   , # sequence of upper case letter
                '[a-zA-Z]+' , # sequence of upper case or lower case letter
                 '[A-Z][a-z]+'# one upper case letter followed by lower case letter
                 ] 


multi_re_find(test_patterns,test_phrase)


# In[ ]:


# escape codes
# you can use special escape codes to find specific types of pattern 
# in your data such digits , non digits , white spaces and more
# use ' \ ' example '\d' a digit and '\D' a non digit 


# In[78]:


# \n is a escape code is python 
print('heloo \n new line')


# In[80]:


test_phrase = 'This is string with some numbers 123 and a symbol #hashtag'
test_patterns = [r'\d+', # squence of digits
                 r'\D+', # squence of non-digits
                 r'\s+', # squence of white space
                 r'\S+', # squence of non white space
                 r'\w+', # alpha numeric character eg . # will be excluded in this
                 r'\W+', # non alpha numeric character eg . # will be include in it
                 ] 
multi_re_find(test_patterns,test_phrase)


# In[ ]:




