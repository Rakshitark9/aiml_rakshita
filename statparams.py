#!/usr/bin/env python
# coding: utf-8

# In[13]:


def mean_value(given_list):
    total = sum(given_list)
    average_value = total/len(given_list)
    return average_value


# In[21]:


mean_value([23,45,33,12])


# In[75]:


def mode_value(L):
    s = set(L)
    d = {}
    for x in s:
        d[x] = L.count(x)
    m=max(d.values())
    for k in d.keys():
        if d[k] == m:
            return k


# In[77]:


L = ["M","N","L","P","M","B","M"]
mode_value(L)


# In[79]:


L = [2,3,4,6,3,7,8,2,6,4,6,3,2,6]
mode_value(L)


# In[ ]:




