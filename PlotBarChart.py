import matplotlib as mpl
import numpy as np

# Use the pgf backend (must be set before pyplot imported)
mpl.use('pgf')

import matplotlib.pyplot as plt
fig = plt.figure()
bremen_runtimes = [17517.92007, 17686.26381] 
household_runtimes = [6951.208566, 8381.653595]
barWidth = 0.2
x = ['Non vectorized HPDB', 'Vectorized HPDBSCAN', ]

# Set position of bar on X axis 
br1 = np.arange(len(bremen_runtimes)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 

# Make the plot
plt.bar(br1, bremen_runtimes, color ='r', width=barWidth, edgecolor ='grey', label ='Non vectorized HPDBSCAN') 
plt.bar(br2, household_runtimes, color ='g', width=barWidth, edgecolor ='grey', label ='Vectorized HPDBSCAN') 
 
plt.ylabel('Mean runtime') 
plt.xticks([r + 0.15 for r in range(len(bremen_runtimes))], 
        ['Bremen dataset', 'Household power dataset'])
 
fig.set_size_inches(8, 9, forward=True)
plt.legend(loc="upper center", 
                          bbox_transform=plt.gcf().transFigure)
plt.show() 
#plt.rc('text', usetex=True)
plt.savefig('single_core_perf_comparison.pgf', format='pgf')
        

