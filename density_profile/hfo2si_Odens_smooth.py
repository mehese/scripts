#! /usr/bin/env python

import sys
from astools.analysis import *
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz

def testGauss(x, y):
    b = gaussian(30, 7.4)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

def O_dens(struct, deltaz, no_points=200, full=False):
    """similar to astools.analysis.vertical_density_profile but only offers the
    vertical density for O only -- used to show the migration of O towards the
    interface layer
    """
    z = np.linspace(-0.5*struct.coordz, 1.5*struct.coordz, 2*no_points)
    rho = np.zeros(2*no_points)

    work_struct = repeat(struct, 1, 1, 3)
    for at in work_struct.atoms:
        at.z = at.z - struct.coordz

    for i in range(len(z)):
        for at in work_struct.atoms:
            if (z[i] - deltaz < at.z < z[i] + deltaz) and (at.species == 'O'):
                rho[i] = rho[i] + mass_dict[at.species]

    # works for orthorhombic cells only, 1.66 -- conversion to g/cm^3 
    volume = 2*deltaz*struct.coordx*struct.coordy/1.66

    # full returns the whole array, full=False only the z=0, z=zmax one
    if full:
        return z, rho/volume
    else:
        return (z[int(0.5*no_points): int(1.5*no_points)], 
                rho[int(0.5*no_points): int(1.5*no_points)]/volume)


print 'amorphous'
cell = ReadStruct('../crystal_files/INPUT_aHfO2', 'crystal')
x, y = O_dens(cell, .5, no_points=230, full=False) 
#plt.plot(x+11.5, testGauss(x, y), 'r-', label='amorphous hafnia (bulk)', linewidth=3)
plt.plot(np.linspace(11.5, 11.5+10.2322, len(x)), testGauss(x, y), 'r-', label='amorphous hafnia (bulk)', linewidth=3)

print 'cell 1...'
cell = ReadStruct('../crystal_files/INPUT_hfo2si_c1', 'crystal')
x, y = O_dens(cell, .5, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), 'k-', label='cell 1')
#plt.plot(x, y, 'k--', label='cell 1')

print 'cell 1 ox...'
cell = ReadStruct('../crystal_files/INPUT_hfo2si_c1ox', 'crystal')
x, y = O_dens(cell, .5, no_points=230, full=True) 
#plt.plot(x, y, 'k-', label='cell 1')
plt.plot(x-2., testGauss(x, y), 'k--', label='cell 1 ox')

print 'cell 2 ox...'
cell = ReadStruct('../crystal_files/INPUT_hfo2si_c2ox', 'crystal')
x, y = O_dens(cell, .5, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), 'k:', label='cell 2 ox')

print 'cell 3 ox...'
cell = ReadStruct('../crystal_files/INPUT_hfo2si_c3ox', 'crystal')
x, y = O_dens(cell, .5, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), 'k-.', label='cell 3 ox')


plt.xlabel(r'z coordinate [$\mathbf{\AA}$]', fontweight='bold', fontsize=25)
plt.ylabel(r'density of O atoms [g/cm$^\mathbf{3}$]', fontweight='bold', fontsize=25)

plt.xlim([0, cell.coordz])
plt.ylim([0, 3])


plt.legend(fontsize=20, loc='upper center', ncol=8)
l = plt.gca().get_legend().get_frame().set_linewidth(2)


minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(20., 7.)
plt.savefig('Odens_hfo2si.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'
