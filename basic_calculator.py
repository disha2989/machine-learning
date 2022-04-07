#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(n1,n2):
    return n1+n2


# In[2]:


def subtract(n1,n2):
    return n1-n2


# In[3]:


def multiply(n1,n2):
    return n1*n2


# In[4]:


def divide(n1,n2):
    return n1/n2


# In[5]:


print("select operation no-\n"     "1.add"     "2.subtract"     "3.multiply"     "4.divide\n")


# In[7]:


select=int(input("select operation from 1,2,3,4\n"))


# In[8]:


print("enter two numbers")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))


# In[16]:


if select == 1:
    print(n1,"+",n2,"=",add(n1,n2))
elif select == 2:
    print(n1,"-",n2,"=",subtract(n1,n2))
elif select == 3:
    print(n1,"x",n2,"=",multiply(n1,n2))
elif select == 4:
    print(n1,"/",n2,"=",divide(n1,n2))    





