#!/usr/bin/env python
# coding: utf-8

# In[27]:


a,b=[int(i) for i in input().split()]
c=0
while a<=b:
    a*=3
    b*=2
    c+=1
print(c)

