def rad2bt(wn,radiance):
	"""
	Computes brightness temperature given wavenumbers and radiances.
	
	 Inputs:
		wn		  wavenumbers (Nx1) in 1/cm 		radiance  radiances (Nx1) in mW/(m^2 sr. 1/cm)
	
	 Outputs:
		bt	  computed brightnes temperature (Nx1) in Kelvin		from DCT 11/11-99
	....Adapted for Python by Von P. Walden
	                          20 January 2011	
	  fundamental constants:	    (Cohen, E.R. and B.N. Taylor, The 1986 CODATA recommended values	     of the fundamental physical constants, Journal of Research of	     the National Bureau of Standard, 92(2), March-April 1987.)
	"""
	from numpy import log
	
	h = 6.6260755e-34  # Planck constant in Js	c = 2.99792458e8   # photon speed in m/s	k = 1.380658e-23   # Boltzmann constant in J/K	
	c1 = 2*h*c*c*1e8
	c2 = h*c/k*1e2	
	bt = c2*wn / (log(1 + (c1*pow(wn,3)) / (radiance/1000.)))
	
	return bt
