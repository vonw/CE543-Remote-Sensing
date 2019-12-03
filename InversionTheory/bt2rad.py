def bt2rad(wn,bt):
	"""

	Computes radiance given wavenumbers and brightness temperature.

	

	 Inputs:

		wn		  wavenumbers (Nx1) in 1/cm 
		bt        brightnes temperature (Nx1) in Kelvin

	
	 Outputs:
        radiance  Planck radiances (Nx1) in mW/(m^2 sr. 1/cm)

    see also RADTOT.M, RAD2BT.M, TTORAD.M
	
	from DCT 11/11-99

	....Adapted for Python by Von P. Walden
	                          27 June 2011
	

	  fundamental constants:
	    (Cohen, E.R. and B.N. Taylor, The 1986 CODATA recommended values
	     of the fundamental physical constants, Journal of Research of
	     the National Bureau of Standard, 92(2), March-April 1987.)

	"""
	import numpy as np
	
	h = 6.6260755e-34  # Planck constant in Js
	c = 2.99792458e8   # photon speed in m/s
	k = 1.380658e-23   # Boltzmann constant in J/K
	

	C1 = 2*h*c*c*1e8

	C2 = h*c/k*1e2
	
	radiance = 1000. * C1 * (wn*wn*wn) / (np.exp((C2*wn)/bt)-1)
	
	return radiance

