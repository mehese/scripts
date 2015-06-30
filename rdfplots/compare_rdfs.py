#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pylab as plt

struct = ReadStruct('INPUT_monoclinic', 'crystal')
#struct = ReadStruct('INPUT_Si_Prim', 'crystal')
struct2 = ReadStruct('INPUT_HfO2_am_init', 'crystal')
struct3 = ReadStruct('INPUT_HfO2_am_fin', 'crystal')
structx = ReadStruct('INPUT_HfO2_am_anneal2', 'crystal')
structy = ReadStruct('INPUT_HfO2_am_anneal3', 'crystal')
structz = ReadStruct('INPUT_HfO2_am_anneal4', 'crystal')

#struct = expand2(struct, X=(-2.2, 2.5), Y=(-3.2, 2.6), Z=(-1.2, 2.))
#PrintStruct(struct, 'crystal_inp', name='CRYSTAL_t_exp')
x, y = rdf_triclinic(struct, 200, dist=10., verbose=True)
y = [np.array(c[:-1]) for c in y]
y = y[0]+y[1]
x2, y2 = rdf2(struct2, 200, dist=10.)
y2 = [np.array(c[:-1]) for c in y2]
y2 = y2[0]+y2[1]
x3, y3 = rdf2(struct3, 200, dist=10.)
y3 = [np.array(c[:-1]) for c in y3]
y3 = y3[0]+y3[1]

xa, ya = rdf2(structx, 200, dist=10.)
ya = [np.array(c[:-1]) for c in ya]
ya = ya[0]+ya[1]

xb, yb = rdf2(structy, 200, dist=10.)
yb = [np.array(c[:-1]) for c in yb]
yb = yb[0]+y3[1]

xc, yc = rdf2(structz, 200, dist=10.)
yc = [np.array(c[:-1]) for c in yc]
yc = yc[0]+yc[1]

#int1 = np.trapz(y, x=x)
#int2 = np.trapz(y2, x=x2)
#int3 = np.trapz(y3, x=x3)

plt.plot(x, y, 'r', label='Monoclinic total', linewidth=0.3)
plt.plot(x2, y2, 'g-', label='Amorphous HfO2, before DFT opt',
         linewidth=1)
#plt.plot(x3, y3, '-', label='Amorphous HfO2, after DFT opt', linewidth=1,
#         color='0.4')
plt.plot(xa, ya, label='Amorphous HfO2, 15000ps, 7000K-200K', color='#f366f4')
plt.plot(xb, yb, label='Amorphous HfO2, 15000ps, 8000K-2000K', color='#3321db')
plt.plot(xc, yc, label='Amorphous HfO2, 35000ps, 9000K-2000K', color='#808020')
plt.title('Total RDF')
plt.xlabel('Distance Angstroem $\\AA$')
plt.legend()
plt.show()
#PrintStruct(struct, 'crystal_inp', name='CRYSTAL_t_rep')
print 'Done!'
