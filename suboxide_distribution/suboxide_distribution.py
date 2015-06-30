#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division
import sys
import os
import matplotlib.pylab as plt
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *

def get_suboxide(struct):
    si1, si2, si3  = [], [], []
    for at in struct.atoms:
        if at.species == 'Si':
            nb = get_neighbours(at, struct, dmax=4.)
            sb = len([a for a in nb if a.at.species == 'O'])
            if sb == 1:
                si1.append(at)
            elif sb == 2:
                si2.append(at)
            elif sb == 3:
                si3.append(at)
    print 'Structure done! -------'
    return si1, si2, si3
            

sb1,  sb2,  sb3  = [], [], []
sb1x, sb2x, sb3x  = [], [], []
Vs = []

for name in ['INPUT_1','INPUT_2','INPUT_3','INPUT_4','INPUT_5','INPUT_6']:
    print '---->', name
    str1 = ReadStruct(name, 'crystal')
    a , b, c = get_suboxide(str1)
    sb1.extend([at.z/str1.coordz for at in a])
    sb2.extend([at.z/str1.coordz for at in b])
    sb3.extend([at.z/str1.coordz for at in c])
    Vs.append(str1.volume())

for name in ['INPUT_2_ox','INPUT_3_ox','INPUT_5_ox']:
    print '---->', name
    str1 = ReadStruct(name, 'crystal')
    a , b, c = get_suboxide(str1)
    sb1x.extend([at.z/str1.coordz for at in a])
    sb2x.extend([at.z/str1.coordz for at in b])
    sb3x.extend([at.z/str1.coordz for at in c])
    Vs.append(str1.volume())

Vmed = np.average(Vs)




#print 'Suboxide ratio:'
#tot = len(sb1)+len(sb2)+len(sb3)
#print '{:2.4f} : {:2.4f} : {:2.4f}'.format(len(sb1)/tot, len(sb2)/tot,
#                                           len(sb3)/tot)

dim = 36
z, y1, y2, y3 = (np.linspace(0., 1., dim),np.zeros(dim),np.zeros(dim),np.zeros(dim))
y1x, y2x, y3x = (np.zeros(dim),np.zeros(dim),np.zeros(dim))
dz = z[1]/2.


for i in range(1, dim):
    for coord in sb1:
        if z[i]-dz < coord < z[i]+dz :
            y1[i] += 1.
    for coord in sb2:
        if z[i]-dz < coord < z[i]+dz :
            y2[i] += 1.
    for coord in sb3:
        if z[i]-dz < coord < z[i]+dz :
            y3[i] += 1.
    for coord in sb1x:
        if z[i]-dz < coord < z[i]+dz :
            y1x[i] += 1
    for coord in sb2x:
        if z[i]-dz < coord < z[i]+dz :
            y2x[i] += 1
    for coord in sb3x:
        if z[i]-dz < coord < z[i]+dz :
            y3x[i] += 1



y1 = map(lambda p: p/(Vmed/(dim*6)), y1) # 6 -- number of structures considered
y2 = map(lambda p: p/(Vmed/(dim*6)), y2)
y3 = map(lambda p: p/(Vmed/(dim*6)), y3)
y1x = map(lambda p: p/(Vmed/(dim*3)), y1x) # 3 -- number of structures considered
y2x = map(lambda p: p/(Vmed/(dim*3)), y2x)
y3x = map(lambda p: p/(Vmed/(dim*3)), y3x)

plt.subplot(2, 1, 1)
plt.xlim([0,1])
plt.text(0.6, 1.5, 'Clean Si', weight='bold',fontsize=18)
plt.ylabel(r"suboxide density [$\AA^{-3}$]", fontsize=14)
plt.plot(z, y1, 'r-', linewidth=2, alpha=0.8, label='Si1+', zorder=0)
plt.plot(z, y2, 'b-', linewidth=2, alpha=0.8, label='Si2+', zorder=1)
plt.plot(z, y3, 'g-', linewidth=2, alpha=0.8, label='Si3+', zorder=2)
plt.legend(bbox_to_anchor=(0.3, 1.1), shadow=True, fancybox=True)
#plt.fill_between(z, y1, facecolor='red', alpha=0.4)
plt.subplot(2, 1, 2)
plt.xlim([0,1])
plt.xlim([0,2])
plt.text(0.6, 0.28, 'Oxidised Si', weight='bold',fontsize=18)
plt.plot(z, y1x, 'r-', linewidth=2, alpha=0.8, label='Si1+', zorder=0)
plt.plot(z, y2x, 'b-', linewidth=2, alpha=0.8, label='Si2+', zorder=1)
plt.plot(z, y3x, 'g-', linewidth=2, alpha=0.8, label='Si3+', zorder=2)
plt.xlabel(r"$\mathbf{z}$ axis fractional position", fontsize=18)
plt.ylabel(r"suboxide density [$\AA^{-3}$]", fontsize=14)
plt.show()
