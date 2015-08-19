#! /usr/bin/python2.7

# cf https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

import numpy as np
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
import matplotlib.animation as animation

name = 'hfo2si_c1ox'
s = ReadStruct('../../crystal_files/INPUT_'+name)
no_frames, atom_iterator = len(s), (p for p in range(len(s)))
def at_it():
    i = 0
    while True:
        yield i % no_frames
        i += 1
atom_iterator = at_it()

for at in s.atoms:
    print at

print 'Anime time!'


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-5, 1), ylim=(-60, 60))
line1, = ax.plot([], [], lw=2, label='atom projection', zorder=1)
line2, = ax.plot([], [], lw=2, zorder=2)

a = np.loadtxt('../../../PDOS_files/'+name+'_1.dat')
ax.plot(a[:,0], a[:,1], color='#0033ff', alpha=0.1, label='Bulk Si',
        linewidth=2, zorder=99)
ax.plot(a[:,0], a[:,3], color='#0033ff', alpha=0.1,
        linewidth=2, zorder=99)

txt = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=20)

# initialization function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line1.set_color('crimson')
    line2.set_color('crimson')
    txt.set_text('')
    return line1, line2, txt

# animation function.  This is called sequentially
def animate(i):
    p = int(next(atom_iterator) + 1)
    #print p
    b = np.loadtxt('../../../PDOS_files/'+name+'_'+str(p)+'.dat')
    x = b[:,0]
    line1.set_data(x, b[:,2])
    line2.set_data(x, b[:,4])
    at_sp = s.atoms[p-1].species
    if at_sp == 'Si':
        line1.set_color('#568A9C')
        line2.set_color('#568A9C')
    elif at_sp == 'Hf':
        line1.set_color('#B85F40')
        line2.set_color('#B85F40')
    else :
        line1.set_color('crimson')
        line2.set_color('crimson')

    txt.set_text('{:3} {:4}'.format(p, at_sp))
    return line1, line2, txt

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1*no_frames, repeat=False, interval=50, blit=True)

#plt.legend()
#plt.show()

#anim.save('file.mp4', fps=2, extra_args=['-vcodec', 'libx264'])
anim.save('file.gif', writer='imagemagick')

print 'Done'

