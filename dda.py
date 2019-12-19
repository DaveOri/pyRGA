import subprocess as sub
import numpy as np
import pandas as pd

c=299792458.0 # m/s

def run_dda(frequency, refractive_index, shapefile, dipole_resolution):
	## Setup DDA command
	savedirectory = 'dda_rga_comp'

	wl = c/frequency
	k = 2.0*np.pi/wl
	wavelength = '-lambda '+str(wl) # meters

	n = refractive_index
	refractive_index = '-m '+str(n.real)+' '+str(n.imag)

	shapecmd = '-shape read ' + shapefile

	dipoles = np.loadtxt(shapefile)
	N = dipoles.shape[0] # number of lines
	effective_radius = k*dipole_resolution*np.cbrt(4.0*np.pi/(3.0*N))
	sizecmd = '-dpl '+str(wl/dipole_resolution)#'-eq_rad ' + str(effective_radius)

	path_to_adda = '/net/ora/develop/adda/src/mpi/adda_mpi'
	number_of_processors = 4

	polarization = '-pol ldr' # lattice dispersion relation might be better for dry snow
	interaction = '-int fcd'
	iterative_method = '-iter qmr2'
	savecmd = '-dir ' + savedirectory
	options = ''

	commands = ['mpirun -np ', str(number_of_processors),
	            path_to_adda,
	            wavelength,
	            refractive_index,
	            shapecmd,
	            sizecmd,
	            polarization,
	            interaction,
	            iterative_method,
	            savecmd,
	            options
	           ]

	## Check and execute
	print(' '.join(commands))
	sub.run(' '.join(commands), check=True, shell=True)

	## Get scattering properties
	mueller = pd.read_csv(savedirectory + '/mueller', sep=' ', index_col='theta')
	back = mueller.loc[180.0]
	sig_bk  = (2*np.pi*(back.s11+back.s22+2*back.s12)/k**2.)
	
	return sig_bk