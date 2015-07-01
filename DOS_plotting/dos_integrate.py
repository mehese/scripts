import numpy as np
import matplotlib.pylab as plt


def doscalc(filename, emin=None, emax=None):
  dat = np.loadtxt(filename)
  if emin == None:
      imin=0
  elif dat[0,0] > emin:
      print '!!! given emin < minimum {}'.format(dat[0,0])
  else:
      i = 0
      while dat[i,0] < emin:
          i+=1  
      imin = i
  
  if (emax == None) or (dat[-1,0] < emax):
      imax=-1
  else:
      i = 0
      while dat[i,0] < emax:
          i+=1  
      imax = i


  #plt.plot(dat[:,0], dat[:,1], 'r-')
  #plt.show()
  return np.trapz(dat[imin:imax,1], x=dat[imin:imax,0])

x1 = doscalc('unpass.dat', emin=-4., emax=-1.)
x2 = doscalc('pass.dat', emin=-4., emax=-1.)
print 'unpass = {:10.5f}\n  pass = {:10.5f}'.format(x1, x2)
u = np.loadtxt('unpass.dat')
plt.plot(u[:,0], u[:,1], label='Unpassivated')
p = np.loadtxt('pass.dat')
plt.plot(p[:,0], p[:,1], label='Passivated')
plt.legend()
plt.show()