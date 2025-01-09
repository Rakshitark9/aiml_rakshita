#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greet(name):
    print(f" Good morning {name}")
greet("Ramya")


# In[3]:


greet = lambda name: print(f"Good morning {name} !")


# In[5]:


greet("Sowmya")


# In[7]:


product = lambda a,b,c : a*b*c
product(20,30,40)


# In[9]:


even = lambda L:[x for x in L if x%2==0]


# In[11]:


my_list = [100,3,9,34,25]
even(my_list)


# In[13]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum/counter
    return mean


# In[15]:


mean_value(3,24,5)


# In[17]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[19]:


product(3,7,9)


# In[ ]:




