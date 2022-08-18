#!/usr/bin/env python
# coding: utf-8

# In[24]:


a=input().lower()
b=''
for i in a:
    if i not in b:
        b+=i
if len(b)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

