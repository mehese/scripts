#! /usr/bin/python2.7

import numpy as np
from astools.ReadWrite import ReadStruct

import matplotlib.pylab as plt

name = 'hfo2si_c1'
s = ReadStruct('../../crystal_files/INPUT_'+name)
frames, atom_iterator = len(s), (p for p in range(len(s)))
for at in s.atoms:
    print at

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-5, 1), ylim=(-60, 60))

c = np.loadtxt('../../../PDOS_files/'+name+'_1.dat')
ax.plot(c[:, 0], c[:, 1], color='blue')
ax.plot(c[:, 0], c[:, 3], color='blue')

y1 = np.zeros(len(c))
y2 = np.zeros(len(c))

for p in range(len(s)):
    i = p+1
    print i
    c = np.loadtxt('../../../PDOS_files/'+name+'_'+str(i)+'.dat')
    y1 += c[:, 2]
    y2 += c[:, 4]
    
plt.plot(c[:,0], y1, color='red')
plt.plot(c[:,0], y2, color='green')

plt.show()
