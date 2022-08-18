#!/usr/bin/env python
# coding: utf-8

# In[29]:


a,b,c=[int(i) for i in input().split()]
s=0
for i in range(1,c+1):
    s+=(a*i)
print(s-b)


# In[ ]:




