#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest


# In[4]:


def cap_text(text):
    return text.capitalize()


# In[5]:


cap_text("uzair")


# In[7]:


class TestCap(unittest.TestCase):
    
#     test case 1
    def test_one_word(self):
        text = 'uzair'
        result = cap_text("uzair")
        self.assertEqual(result,text)
        
#       test case 2

    def text_many_word(self):
        text = 'my name is uzair'
        result = cap_text("my name is uzair")
        self.assertEqual(result,text)
    
        


# In[12]:


# __name__ == '__main__' : this will return that either module is imported or not if yes than it will reutrn yes

if __name__ == '__main__' :
    unittest.main()
        

    


# In[ ]:




