import numpy as np
import matplotlib.pyplot as plt
import random


X=[14,15,16,17,18,19,20,21]
P=[0.133,0.0667,0.133,0.2,0.0667,0.133,0.2,0.0667]
plt.stem(X,P,linefmt='green',label='Theortical PMF')

x=[]
P=[]
for i in range(15):
    x.append(random.randint(14,21))
for i in range(8):
    c=0
    for j in range(15):
        if x[j]==14+i:
            c=c+1
    prob=c*(1/15)
    P.append(prob)
plt.stem(X,P,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X')
plt.ylabel('P(X=x)')
plt.title('PMF of X')
plt.legend()
plt.show()  
  
        
    