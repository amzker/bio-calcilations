#usr/bin/python3
#For Calculating Km & Vmax in nonlinearity using math method
import matplotlib.pyplot as plt
import numpy as np
import pylab
D1 = int(input("Enter Value of DR1 : "))
D2 = int(input("Enter Value of DR2 : "))
C1 = float(input("Enter Value of Css1: "))
C2 = float(input("Enter Value of Css2: "))

FD = D2 - D1
FDR = D1/C1
FDRS= D2/C2
xx = FDR - FDRS
k =  FD/xx

print("Km: ",k)

zz = k*D1/C1
V = D1+zz
print("Vmax : ",V)
#C = pylab.linspace(0, 2, 1000)
C = 15
def rate(D, k , V):
    return V*C/k+C

#C = pylab.linspace(0, 2, 1000)
pylab.plot(C, rate(C1, k, V ))
#pylab.plot(rate(C2, k, V))
pylab.show()

#plt.plot(rate(D1 ,k, V)         
#plt.plot(rate(D2 ,k, V)
#plt.xlabel("Css")
#plt.ylabel("DR")
#plt.title("direct plot")
#plt.show()
