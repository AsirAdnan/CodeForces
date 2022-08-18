#!/usr/bin/env python
# coding: utf-8

# In[31]:


a,b,c=[int(i) for i in input().split()]
s=0
for i in range(1,c+1):
    s+=(a*i)
if s-b<0:
    print(0)
else:
    print(s-b)


# In[ ]:




