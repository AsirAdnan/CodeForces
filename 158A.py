#!/usr/bin/env python
# coding: utf-8

# In[6]:


x,y=[int(i) for i in input().split()]
l=[int(j) for j in input().split()]
x=l[y-1]
count=0
for k in l:
    if k>=x and k>0:
        count+=1
print(count)


# In[ ]:




