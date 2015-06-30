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
    print len(si1), len(si2), len(si3)
    print 'Structure done! -------'
    return si1, si2, si3
            

sb1, sb2, sb3  = [], [], []
for name in ['INPUT_2_ox','INPUT_3_ox','INPUT_5_ox']:
    print '---->', name
    str1 = ReadStruct(name, 'crystal')
    a , b, c = get_suboxide(str1)
    sb1.extend([at.z/str1.coordz for at in a])
    sb2.extend([at.z/str1.coordz for at in b])
    sb3.extend([at.z/str1.coordz for at in c])

print 'Suboxide ratio:'
tot = len(sb1)+len(sb2)+len(sb3)
print '{:2.4f} : {:2.4f} : {:2.4f}'.format(len(sb1)/tot, len(sb2)/tot,
                                           len(sb3)/tot)

dim = 65
z, y1, y2, y3 = (np.linspace(0., 1., dim),np.zeros(dim),np.zeros(dim),np.zeros(dim))
dz = z[1]/2

print '-'*70
#print sb1
print sb2
print sb3
print '-'*70

for i in range(1, dim):
    for coord in sb1:
        if z[i]-dz < coord < z[i]+dz :
            y1[i] += 1
    for coord in sb2:
        if z[i]-dz < coord < z[i]+dz :
            y2[i] += 1
    for coord in sb3:
        if z[i]-dz < coord < z[i]+dz :
            y3[i] += 1

mx1 = max(y1) 
mx2 = max(y2) 
mx3 = max(y3) 
y1 = map(lambda p: 2*p/mx1, y1)
y2 = map(lambda p: 2*p/mx2, y2)
y3 = map(lambda p: 2*p/mx3, y3)

#print y1
print y2
print y3

plt.xlabel("$z$ axis fractional position", fontsize=18)
plt.xlim([0,1])
plt.ylim([0,2.3])
plt.title('Suboxide distribution')
plt.plot(z, y1, 'r-', linewidth=2, alpha=0.8, label='Si1+', zorder=0)
plt.plot(z, y2, 'b-', linewidth=2, alpha=0.8, label='Si2+', zorder=1)
plt.plot(z, y3, 'g-', linewidth=2, alpha=0.8, label='Si3+', zorder=2)
#plt.fill_between(z, y1, facecolor='red', alpha=0.4)
plt.legend(loc=2)
plt.show()
