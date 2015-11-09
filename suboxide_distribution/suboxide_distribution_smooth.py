#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('/home/eric/Dropbox/astools/')
from astools.analysis import *
from matplotlib.ticker import MultipleLocator
from matplotlib import rc
from scipy.interpolate import spline

def get_suboxide(struct):
    si1, si2, si3  = [], [], []
    for at in struct.atoms:
        if at.species == 'Si':
            # Returns the nearest 4 neighbours where nb.at is an Atom object and
            # nb.d is the distance from the current atom (at from struct.atoms)
            nb = get_neighbours(at, struct, dmax=4.)
            # Total number of O atoms in the nearest 4 neighbours that are
            # bonded to the Si atom (i.e d < 1.9 Angstroem)
            sb = len([a for a in nb if a.at.species == 'O' and a.length < 1.9])
            # Si1+
            if sb == 1:
                si1.append(at)
            # Si2+
            elif sb == 2:
                si2.append(at)
            # Si3+
            elif sb == 3:
                si3.append(at)
    print 'Structure done! -------'
    return si1, si2, si3
            

sb1,  sb2,  sb3  = [], [], []
sb1x, sb2x, sb3x  = [], [], []
# list containing the volumes of the analysed structures
Vs = []
# list containing the xy cross section area of the analysed structrures
As = []

maxz=20.

for name in ['INPUT_1','INPUT_2','INPUT_3','INPUT_4','INPUT_5','INPUT_6']:
    print '---->', name
    str1 = ReadStruct(name, 'crystal')
    # plot will range to the maximum obtained z coordinate
    maxz = str1.coordz if str1.coordz > maxz else maxz

    a , b, c = get_suboxide(str1)
    sb1.extend([at.z for at in a])
    sb2.extend([at.z for at in b])
    sb3.extend([at.z for at in c])

    Vs.append(str1.volume())
    As.append(str1.coordx*str1.coordy)

for name in ['INPUT_2_ox','INPUT_3_ox','INPUT_5_ox']:
    print '---->', name
    str1 = ReadStruct(name, 'crystal')
    # plot will range to the maximum obtained z coordinate
    maxz = str1.coordz if str1.coordz > maxz else maxz

    a , b, c = get_suboxide(str1)
    sb1x.extend([at.z for at in a])
    sb2x.extend([at.z for at in b])
    sb3x.extend([at.z for at in c])

    Vs.append(str1.volume())
    As.append(str1.coordx*str1.coordy)




print 'Suboxide ratio clean:'
tot = len(sb1)+len(sb2)+len(sb3)
print '{:2.4f} : {:2.4f} : {:2.4f}'.format(len(sb1)/tot, len(sb2)/tot,
                                           len(sb3)/tot)
print 'Suboxide ratio ox:'
tot = len(sb1x)+len(sb2x)+len(sb3x)
print '{:2.4f} : {:2.4f} : {:2.4f}'.format(len(sb1x)/tot, len(sb2x)/tot,
                                           len(sb3x)/tot)

print 'Suboxide surface density'
tot = len(sb1)+len(sb2)+len(sb3)+len(sb1x)+len(sb2x)+len(sb3x)
surf = 2*sum(As)
print '{} suboxides/{:10.5} Å²  = {:10.5f} Å⁻²'.format(tot, surf, tot/surf)


dim = 46
z, y1, y2, y3 = (np.linspace(0., maxz, dim),np.zeros(dim),np.zeros(dim),np.zeros(dim))
y1x, y2x, y3x = (np.zeros(dim),np.zeros(dim),np.zeros(dim))
dz = 1.5

# volume considered for each defect
Vmed = np.average(As)*2*dz


for i in range(1, dim):
    for coord in sb1:
        if z[i]-dz < coord < z[i]+dz :
            y1[i] += 1./Vmed
    for coord in sb2:
        if z[i]-dz < coord < z[i]+dz :
            y2[i] += 1./Vmed
    for coord in sb3:
        if z[i]-dz < coord < z[i]+dz :
            y3[i] += 1./Vmed

    for coord in sb1x:
        if z[i]-dz < coord < z[i]+dz :
            y1x[i] += 1./Vmed
    for coord in sb2x:
        if z[i]-dz < coord < z[i]+dz :
            y2x[i] += 1./Vmed
    for coord in sb3x:
        if z[i]-dz < coord < z[i]+dz :
            y3x[i] += 1./Vmed






y1 = map(lambda p: p/6, y1) # 6 -- number of clean structures considered
y2 = map(lambda p: p/6, y2)
y3 = map(lambda p: p/6, y3)
y1x = map(lambda p: p/3, y1x) # 6 -- number of oxidised structures considered
y2x = map(lambda p: p/3, y2x)
y3x = map(lambda p: p/3, y3x)

dim = 200
z_ = np.linspace(0, maxz, dim)
y1new = spline(z, y1, z_)
y2new = spline(z, y2, z_)
y3new = spline(z, y3, z_)
y1oxnew = spline(z, y1x, z_)
y2oxnew = spline(z, y2x, z_)
y3oxnew = spline(z, y3x, z_)

# Plot clean cells
minor_locator = MultipleLocator(1)

plt.subplot(2, 1, 1)

plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().yaxis.labelpad = 30 
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.xlim([0,maxz])
plt.ylim([0,0.018])
plt.text(14.6, .014, 'Unoxidised Si cells', weight='bold',fontsize=24)
plt.ylabel(r"suboxide density [$\mathbf{\AA^{\mathbf{-3}}}$]", fontweight='bold', fontsize=25)
#plt.plot(z, y1, 'r-', linewidth=2, alpha=0.8, label=r'Si$^{1+}$', zorder=0)
plt.plot(z_, y1new, 'r-', linewidth=3.5, alpha=0.8, label=r'Si$^{1+}$', zorder=0)
#plt.plot(z, y2, 'b-', linewidth=2, alpha=0.8, label='Si2+', zorder=1)
plt.plot(z_, y2new, 'b-', linewidth=3.5, alpha=0.8, label=r'Si$^{2+}$', zorder=1)
#plt.plot(z, y3, 'g-', linewidth=2, alpha=0.8, label='Si3+', zorder=2)
plt.plot(z_, y3new, 'g-', linewidth=3.5, alpha=0.8, label=r'Si$^{3+}$', zorder=2)
# this will function as a legend for both graphs
plt.legend(bbox_to_anchor=(0.3, 0.9), shadow=True, fancybox=True, fontsize=26)

# Plot oxidised cells
plt.subplot(2, 1, 2)

plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().yaxis.labelpad = 30 
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.xlim([0,maxz])
plt.ylim([0,0.018])
plt.text(14.6, .014, 'Oxidised cells', weight='bold',fontsize=24)
plt.ylabel(r"suboxide density [$\mathbf{1/\AA^{3}}$]", fontweight='bold', fontsize=25)
#plt.plot(z, y1x, 'r-', linewidth=2, alpha=0.8, label='Si1+', zorder=0)
plt.plot(z_, y1oxnew, 'r-', linewidth=3.5, alpha=0.8, label='Si1+', zorder=0)
#plt.plot(z, y2x, 'b-', linewidth=2, alpha=0.8, label='Si2+', zorder=1)
plt.plot(z_, y2oxnew, 'b-', linewidth=3.5, alpha=0.8, label='Si2+', zorder=1)
#plt.plot(z, y3x, 'g-', linewidth=2, alpha=0.8, label='Si3+', zorder=2)
plt.plot(z_, y3oxnew, 'g-', linewidth=3.5, alpha=0.8, label='Si3+', zorder=2)

plt.xlabel(r'z coordinate [$\mathbf{\AA}$]', fontweight='bold', fontsize=25)
plt.ylabel(r"suboxide density [$\mathbf{\AA^{\mathbf{-3}}}$]", fontsize=25)


plt.gcf().set_size_inches(20., 14.)
plt.savefig('suboxide_distribution.png', dpi=100, bbox_inches='tight')
#plt.show()
print 'Done!'
