import numpy as np
import matplotlib.pyplot as plt
import pamtra2.libs.refractiveIndex as ref
from dda import run_dda
from rga import run_rga

## INPUT parameters

frequency = 5.6e9 # Hertz
temperature = 270.0 # Kelvin
shapefile = 'aggregate_regular.txt'
#shapefile = 'dendrite-650e-6-513-0.0-simultaneous-G4yWR8UX.agg'
dipole_resolution = 20e-6 # meters
savedirectory = 'dda_rga_comp'

# n = ref.ice.n(temperature, frequency)
# sig_bk = run_dda(frequency, n, shapefile, dipole_resolution)

# print(sig_bk)
# print(run_rga(frequency, n, shapefile, dipole_resolution))

frequencies = np.linspace(1.0e9, 100.0e9, 100)
sig_bk_rga = []
for f in frequencies:
  n = ref.ice.n(temperature, f)
  sig_bk = run_rga(f, n, shapefile, dipole_resolution)
  sig_bk_rga.append(sig_bk)

freq_dda = np.array([2.8, 5.6, 13.6, 35.6, 94])*1.0e9
sig_bk_dda = []
for f in freq_dda:
  n = ref.ice.n(temperature, f)
  sig_bk = run_dda(f, n, shapefile, dipole_resolution)
  sig_bk_dda.append(sig_bk)

plt.figure()
plt.plot(frequencies, sig_bk_rga)
plt.scatter(freq_dda, sig_bk_dda)
plt.xscale('log')
plt.yscale('log')
plt.show()