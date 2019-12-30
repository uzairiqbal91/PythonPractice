#!/usr/bin/env python
# coding: utf-8

# In[1]:


# we can use error handling to let the script continue with other code , even if there is an error
# try:
#     this block of code to be attempted (may lead an error)

# except:
#     will execute in case there is an error in try block

# finally:
#     A final block of code to be executed , regardless of an error
    


# In[2]:


def sum(num1,num2):
    return num1+num2


# In[3]:


sum(3,4)


# In[6]:


number1 = 10


# In[7]:


number2 = input("please enter number")


# In[10]:


# this will throw an error because input returns in string but we need intger type

sum(number1,number2)

# this will not execute because of an error in previous line

print("hey let me execute")


# In[23]:


try:
    result = 10+"10"

except:
    print("cant add because of unmatch datatype")

else : 
    print("I execute when their is no error")
    
finally:
    print("I always execute")
    

# this will exceute ecen their is an error in previous line
# or put in finally block 
print("hey let me execute")


# In[31]:


def ask_for_int():
    
    while(True):
        try:
            result = int(input("provide a number"))

        except:
            print("whoop thats not a number")
            continue

        else:
            print("Thank you" + "you enterd" + str( result))
            break

        finally:
            print("end of try/except/finally")
            print("I always run in the end")


# In[32]:


ask_for_int()


# In[29]:


ask_for_int()


# In[ ]:




