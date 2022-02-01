#For Calculating Km & Vmax in nonlinearity using direct plot method

import matplotlib.pyplot as plt
import numpy as np

# In[18]:


#day 1
c1 = [9.8]
d1 = [600]
c2 = [28.6]
d2 = [1200]

#day 2

#d2time = [3.4, 5.0]
#d2effect = [2.0,4.0]
#plt.scatter(c1, d1)
plt.plot([c1, d1], label = "Dose 1")
plt.plot([c2, d2], label = "Dose 2")
#zxx = np.linespace(-10,10,500)
#plt.plot(c1 , d1, 'red')
#plt.plot(c2 , d2, 'green')
plt.xlabel("Css")
plt.ylabel("DR")
plt.title("direct plot")
plt.show()


# In[ ]:
