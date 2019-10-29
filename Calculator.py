#!/usr/bin/env python
# coding: utf-8

# In[7]:


equasion = input("Enter the equasion")
number= ''
number2= ''
switch = False
op = ''
operation = {'*','+','/','-'}
for char in equasion:
    if(char.isdigit()):
        if(switch):
            number2+=char
        else:
            number+=char
    elif(char in operation):
        switch = True
        op = char
number_int = int(number)
number2_int = int(number2)
if(op=='*'):
    print(number_int*number2_int)
if(op=='/'):
    print(number_int/number2_int)
if(op=='+'):
    print(number_int+number2_int)
if(op=='-'):
    print(number_int-number2_int)
    


# In[ ]:




