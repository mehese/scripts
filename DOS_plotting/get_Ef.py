#! /usr/bin/python

import os
import numpy as np

eV = lambda k : 27.212*k

with open('OUTPUT', 'r') as f:
	txt = f.read().split('NUMBER OF AO')
	N = int(txt[1][:250].split('\n')[1][25:30])
with open('OUTPUT', 'r') as f:
	txt = f.read().split('SUMMED SPIN DENSITY')
	spin_sum = float(txt[-1].split('\n')[0])

print 'Spin sum = ', spin_sum
print 'Number of electrons per cell =', N

with open('XCBD.DAT.000', 'r') as x:
	print 'Analysing XCBD file...'
	no_bands = N/2
	print 'Number of bands to consider (no elec/2)= ', no_bands
	print 'Number of lines to skip (number bands/4)', no_bands/4
	print 'Number words to go after (number bands%4)', no_bands%4
	txt = x.readlines()	
	no_K = int(txt[1].split()[-1])	
	kpts = os.popen('grep -nr "EIGENVALUES FOR KPOINT" XCBD.DAT.000').readlines()
	no_rows =   int(kpts[1].split()[0][:-1]) - int(kpts[0].split()[0][:-1]) -3
	print 'Rows to read per k-point', no_rows


	fracs, _ = np.modf(spin_sum//2)
	if np.fabs(fracs) > 1e-10:
		print 'SYSTEM IS PROBABLY METALLIC!!!!'
		exit()
	
	spin_sum = int(spin_sum)


	print 'Reading spin ups...'
	ups = []
	#for i in range(no_K):
	for i in range(no_K):
		#print '--- K point --UP-----'+str(i+1)
		starts_at = int(kpts[i].split()[0][:-1])
		f = open('tmp.txt', 'w')
		to_load = ''.join(txt[starts_at:starts_at+no_rows])
		f.write(to_load)
		f.close()
		eigs = np.loadtxt('tmp.txt', dtype=np.float)
		eigs = eigs.reshape(-1)
		#print eigs
		ups.append(eigs)

	print 'Reading spin downs...'
	ds = []
	#for i in range(no_K):
	for i in range(no_K, 2*no_K):
		#print '--- K point --DOWN---'+str(i+1-no_K)
		starts_at = int(kpts[i].split()[0][:-1])
		f = open('tmp.txt', 'w')
		to_load = ''.join(txt[starts_at:starts_at+no_rows])
		f.write(to_load)
		f.close()
		eigs = np.loadtxt('tmp.txt', dtype=np.float)
		eigs = eigs.reshape(-1)
		#print eigs
		ds.append(eigs)
	
	if spin_sum > 0:
		spin_sum //= 2	
		Ef_u = max(eig[no_bands-1+spin_sum] for eig in ups)
		Ef_d = max(eig[no_bands-1] for eig in ds)
		Ef = max(Ef_u, Ef_d)
		print '%20.10f a.u. =  %20.10f eV'%(Ef, eV(Ef))
	elif spin_sum < 0:
		spin_sum //= 2	
		Ef_u = max(eig[no_bands-1] for eig in ups)
		Ef_d = max(eig[no_bands-1+spin_sum] for eig in ds)
		Ef = max(Ef_u, Ef_d)
		print '%20.10f a.u. =  %20.10f eV'%(Ef, eV(Ef))
	else:
		print '\nFermi level at:'
		Ef = max(eig[no_bands-1] for eig in ups+ds)
		print '%20.10f a.u. =  %20.10f eV'%(Ef, eV(Ef))

