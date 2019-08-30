def bt2rad_wv(wv,bt):
	"""

	Computes radiance given wavenumbers and brightness temperature.

	

	 Inputs:

		wv		  wavelength (Nx1) in micrometers 
		bt        brightnes temperature (Nx1) in Kelvin

	
	 Outputs:
        radiance  Planck radiances (Nx1) in mW/(m^2 sr. um)

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

	wl = wv*1e-6       # Convert from micrometers to meters.
	return 2*h*c*c*(wl**-5) / ( np.exp(h*c/(k*wl*bt))-1 ) / 1e6   # Converts from W m-3 to W m-2 um-1 

