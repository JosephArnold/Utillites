import matplotlib as mpl
import numpy as np

# Use the pgf backend (must be set before pyplot imported)
mpl.use('pgf')

import matplotlib.pyplot as plt

A = np.loadtxt('bremen_core_scalability.txt', delimiter='\t')
print(A)
fig = plt.figure()
plt.plot(A[:,0], A[:,1], color='r',  marker='x', label ='Non vectorized HPDBSCAN' )
plt.plot(A[:,0], A[:,2], color='g',  marker='x', label ='Vectorized HPDBSCAN')
plt.ylabel('Speedup') 
plt.xlabel("Number of cores")
plt.legend(loc="lower right")
plt.grid()
plt.show()
plt.savefig('Bremen_core_scalability.pgf', format='pgf')

