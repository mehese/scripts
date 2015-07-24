from math import pi, exp
import scipy as sp
import pylab as plt
from sys import argv

def lrntz(x, x0, gamma):
	return (1/pi)*(gamma/((x - x0)*(x - x0) + gamma*gamma))

print 'Opening file:   ', argv[1]
f = open(argv[1], 'r')
f2 = open('image2.csv', 'r')
f2.readline()

omg_mod = []
rmn_mod = []

for line in f2:
	#print line.split()
	omg_mod = omg_mod + [float(line.split()[0])]
	rmn_mod = rmn_mod + [float(line.split()[1])]


line = ''
omg_m = []
I  = []
omega = sp.arange(90, 900, .5)
I_tot = len(omega)*[0.]

I_Wu = len(omega)*[0.]
Wu_peaks =                    [119., 134., 147., 255., 330., 387., 495., 572., 665., 131., 166., 243., 328., 402., 508., 558., 633., 770.] 
Wu_int = map(lambda x: x*15., [1.4 , 2.0 , 2.4 , 1.4 , 1.  , 2.4 , 8.  , 1.3 , 2.  , 1.4 , 1.4 ,  1. , 1.  , 3.4 , 3.  ,   1.,  2. , 0.8  ])

for i in range(len(omega)):
	for j in range(len(Wu_int)):
		I_Wu[i] = I_Wu[i] + Wu_int[j]*lrntz(omega[i], Wu_peaks[j], 5.)  

###########################################################################################################################
while '+   E N D    O F    R A M A N    I N T E N S I T Y    C A L C U L A T I O N  +' not in line:
	line = f.readline()	 
f.readline()

line = f.readline()
while '+ .......................................................................... +'  not in line:
	if len (line.split()) > 7 and line.split()[7] == 'Y' :
		omg_m  = omg_m + [float(line.split()[2])] 
		I = I + [float(line.split()[6])]
	line = f.readline()

for i in range(len(omega)):
	for j in range(len(omg_m)):
		I_tot[i] = I_tot[i] + I[j]*lrntz(omega[i], omg_m[j], 5.)  
###########################################################################################################################
rmn_mod = map(lambda x: 1./10000*x, rmn_mod) 

plt.grid('on')
plt.xlabel('Wavenumber cm$^{-1}$')
plt.ylabel('Raman Intensity $\\mathrm{\\AA}^4$')
plt.plot(omega, I_tot, 'r-', label = 'Castep Raman')
plt.plot(omega, I_Wu, 'b-', label = 'R. Wu et al, LDA-HGH')
plt.plot(omg_mod, rmn_mod, 'k-', label = 'Modreanu Raman')
plt.fill_between(omega, I_Wu, 0, color='blue', alpha = 0.3)
plt.fill_between(omg_mod, rmn_mod, 0, color='black', alpha = 0.2)
plt.fill_between(omega, I_tot, 0, color='red', alpha = 0.5)
plt.xlim([90,900])
plt.legend()
plt.show()
