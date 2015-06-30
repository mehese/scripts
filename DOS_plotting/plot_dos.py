#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

ev = lambda x: x*27.212

# cell 3 Ef = -2.91 
c3 = np.loadtxt('state_density_57_105_124.dat')
E, dos_u, at57_u, at105_u, at124_u, dos_d, at57_d, at105_d, at124_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_125_134.dat')
_, _, at125_u, at134_u, _, at125_d, at134_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6]

c3 = np.loadtxt('state_density_14_26_69.dat')
_, _, at14_u, at26_u, at69_u, _, at14_d, at26_d, at69_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_58_73_74.dat')
_, _, at58_u, at73_u, at74_u, _, at58_d, at73_d, at74_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_82_120_128.dat')
_, _, at82_u, at120_u, at128_u, _, at82_d, at120_d, at128_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_102_114_142.dat')
_, _, at102_u, at114_u, at142_u, _, at102_d, at114_d, at142_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_126_133_140.dat')
_, _, at126_u, at133_u, at140_u, _, at126_d, at133_d, at140_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

c3 = np.loadtxt('state_density_102_105_114_proj.dat')
_, _, at102x_u, at105x_u, at114x_u, _, at102x_d, at105x_d, at114x_d = c3[:,0], c3[:, 1], c3[:,2], c3[:,3], c3[:,4], c3[:,5], c3[:,6], c3[:,7], c3[:,8]

plt.plot(E, dos_u, color='0.7', label='Total c2', linewidth=0.5)
plt.plot(E, dos_d, color='0.7', linewidth=0.5)

#plt.plot(E, at58_u+at73_u+at74_u+at120_u+at128_u, color='#B8E62E', label='Atoms 58, 73, 74, 120, 128 Si(Si2)', linewidth=2)
#plt.plot(E, at58_d+at73_d+at74_d+at120_d+at128_d, color='#B8E62E', linewidth=2)


plt.plot(E, at102_u+at105_u+at114_u, color='#808080', label='Atoms 102, 105, 114 Si(Si3)', linewidth=2)
plt.plot(E, at102_d+at105_d+at114_d, color='#808080', linewidth=2)
plt.plot(E, at102x_u+at105x_u+at114x_u, color='#660066', label='Atoms 102, 105, 114 Si(Si3) + neighbours', linewidth=2)
plt.plot(E, at102x_d+at105x_d+at114x_d, color='#660066', linewidth=2)


#plt.plot(E, at57_u+at82_u, color='#D4AF19', label='Atoms 57, 82 Si(Si2O)', linewidth=2)
#plt.plot(E, at57_d+at82_d, color='#D4AF19', linewidth=2)
#
#
#plt.plot(E, at126_u+at133_u+at140_u+at142_u, color='#660066', label='Atoms 126, 133, 140, 142 Si(O2)', linewidth=2)
#plt.plot(E, at126_d+at133_d+at140_d+at142_d, color='#660066', linewidth=2)
#
#
#plt.plot(E, at124_u+at125_u+at134_u, color='#0099FF', label='Atoms 124, 125, 134 Si(O3)', linewidth=2)
#plt.plot(E, at124_d+at125_d+at134_d, color='#0099FF', linewidth=2)

#plt.plot(E, at57_u, color='#808080', label='Atom 57 (.54) Si=Si-O', linewidth=2)
#plt.plot(E, at58_u, '--', color='#808080', label='Atom 58 Si=Si-O',
#         linewidth=1.5)
#plt.plot(E, at57_d, color='#808080', linewidth=2)
#plt.plot(E, at58_d, '--', color='#808080',
#         linewidth=1.5)
#
#plt.plot(E, at105_u, color='#B8E62E', label='Atom 105 (-.65) $Pb_0$ 2nd layer', linewidth=2)
#plt.plot(E, at105_d, color='#B8E62E', linewidth=2)
#
#plt.plot(E, at124_u, color='#D4AF19', label='Atom 124 (-.82) $E\'$ near \
#interface', linewidth=2)
#plt.plot(E, at124_d, color='#D4AF19', linewidth=2)
#
#plt.plot(E, at125_u, color='#660066', label='Atom 125 (.43) $E\'$', linewidth=2)
#plt.plot(E, at125_d, color='#660066', linewidth=2)
#
#plt.plot(E, at134_u, color='#0099FF', label='Atom 134 (.39) $E\'$', linewidth=2)
#plt.plot(E, at134_d, color='#0099FF', linewidth=2)
#
#plt.plot(E, at14_u+at26_u+at69_u, color='0.05', label='Near Fermi oxygens', linewidth=2)
#plt.plot(E, at14_d+at26_d+at69_d, color='0.05', linewidth=2)

# Plot Fermi level
#plt.plot([-2.70, -2.70], [-100, 100], '--', color='#ff0000', linewidth=2,
#         label='$E_F$')
Ef=-2.68
plt.plot([Ef, Ef], [-100, 100], '-', color='#e62e00', linewidth=2, label='$E_F$')

plt.title('Cell 2') 
plt.xlabel('Energy (eV)')
plt.ylim([-70,70])
plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=10)
plt.gcf().set_size_inches(10., 7.)
plt.savefig('test2png.png', dpi=100, bbox_inches='tight')
plt.show()
