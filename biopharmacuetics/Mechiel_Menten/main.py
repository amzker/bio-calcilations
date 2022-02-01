#!/usr/bin/env python
# coding: utf-8

# In[136]:


import matplotlib.pyplot as plt
import numpy as np


# In[137]:


D1 = int(input("Enter Value of DR1 : "))
D2 = int(input("Enter Value of DR2 : "))
C1 = float(input("Enter Value of Css1: "))
C2 = float(input("Enter Value of Css2: "))

FD = D2 - D1
FDR = D1/C1
FDRS= D2/C2
xx = FDR - FDRS
K =  FD/xx

print("Km: ",K)

zz = K*D1/C1
V = D1+zz
print("Vmax : ",V)


# In[138]:



#D1, D2 ,C1 , C2 = 600,1200,9.8,28.6
C = np.linspace(0,100, num = 100)
def D(C, V, K):
    return (V*C)/(K+C)

plt.plot(D(C ,V ,K), linestyle = '-')
plt.xlabel("C")
plt.ylabel("D")
plt.plot(K,V/2 , '-s', color = 'black')
plt.axhline(y = V/2, color = 'grey', linestyle = '--')
plt.axvline(x = K, color = 'grey', linestyle = '--')
plt.show()
#D(C,V,K)
#print(D(C,V,K))


# In[139]:

'''
aaprre line space etle array no range 
ne ema num = argument impoort chhe ne eno formula
B-A/NUM chhe 

ex uper nu

100-0/100 = 1 etle par 1 point e graph plot thase

'''
