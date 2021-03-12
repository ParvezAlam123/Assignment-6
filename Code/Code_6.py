import numpy as np
import matplotlib.pyplot as plt

X=[14,15,16,17,18,19,20,21]
P=[0.133,0.0667,0.133,0.2,0.0667,0.133,0.2,0.0667]
plt.stem(X,P,linefmt='green',label='theortical PMF')
plt.xlabel('X')
plt.ylabel('P(X=x)')
plt.title('PMF of X')
plt.show()
