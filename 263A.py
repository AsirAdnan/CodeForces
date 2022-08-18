#!/usr/bin/env python
# coding: utf-8

# In[11]:


l2=[]
for i in range(5):
    l2.append(input().split())
for row in range(5):
    for col in range(5):
        if l2[row][col]=='1':
            r=row
            c=col
            break
print(abs(2-c)+abs(2-r))

