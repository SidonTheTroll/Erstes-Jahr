import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0.,10,0.1)
a = np.cos(x)
b = np.sin(x)

plt.plot(x,a,'b')
plt.plot(x,b,'r') 

plt.show()


#====================================

week = [1,2,3,4]
prices = [40, 80, 60, 50]

plt.plot(week, prices) 
plt.xlabel('Week')
plt.ylabel('Onion Prices (INR)')

plt.show()


#====================================
 
x = np.random.randint(1,100, size = 100) 
y = np.random.randint(1,100, size = 100)

plt.scatter(x,y, color = 'b')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()
