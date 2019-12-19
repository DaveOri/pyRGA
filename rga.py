import numpy as np
import pamtra2.libs.refractiveIndex as ref

c=299792458.0 # m/s

# adda default propagation direction is (0,0,1) aka z-axis
def form_factor(dipoles, dipole_resolution, k):
    z = dipoles[:, 2]
    return (np.exp(complex(0.0, 1.0)*dipole_resolution*z*k*2.0)*dipole_resolution**3).sum()

def run_rga(frequency, refractive_index, shapefile, dipole_resolution):
  ## INPUT parameters

  dipole_resolution = 20e-6 # meters

  wl = c/frequency
  k = 2.0*np.pi/wl
  n = refractive_index
  K2 = np.abs(n-1/(n+2))**2
  dipoles = np.loadtxt(shapefile)
  N = dipoles.shape[0]
  V = N*dipole_resolution**3

  f = form_factor(dipoles, dipole_resolution, k)

  sig_bk = 9*k**4*K2*np.abs(f)**2/(4*np.pi)
  return sig_bk/(4.0*np.pi) # I divide everything by 4pi to match DDA, but I am not sure if it should be there or not
                                     # need to check with SSRGA