# ....Example 1 from Wilson (2012)
from Py6S import *
# Create an object to hold the 6S parameters
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
# Set the atmospheric profile to Tropical
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.Tropical)
# Set the wavelength to 0.357um
s.wavelength = Wavelength(0.357)
# Run the model and print some outputs 
s.run()
print(s.outputs.pixel_radiance)
print(s.outputs.background_radiance)
print(s.outputs.single_scattering_albedo)
print(s.outputs.transmittance_water.downward)


# ....Example 2 from Wilson (2012)
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
wavelengths , results = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
SixSHelpers.Wavelengths.plot_wavelengths(wavelengths , results , r"At-sensor Spectral Radiance ($W/m^2\!/\mu m$)")


# ....Example 2 from Wilson (2012)
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
# Set solar azimuth and zenith angles and wavelength
s.geometry.solar_a = 0
s.geometry.solar_z = 30
s.wavelength = Wavelength(0.550)
# Set the directional ground reflectance to be modeled
# by the Roujean BRDF model, using parameters for a pine forest
# (parameters taken from Roujean et al., 1992)
s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133) 
# Run the model and plot the results, varying the view angle (the other
# option is to vary the solar angle) and plotting the pixel radiance. 
SixSHelpers.Angles.run_and_plot_360(s, 'view', 'pixel_radiance', colorbarlabel=r"At-sensor Spectral Radiance ($W/m^2\!/\mu m$)") 




# ....BRDF of Lambertian surface
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
# Set solar azimuth and zenith angles and wavelength
s.geometry.solar_a = 0
s.geometry.solar_z = 30
s.wavelength = Wavelength(0.550)
# Set the Lambertian ground reflectance
s.ground_reflectance = GroundReflectance.HomogeneousLambertian(1.) 
# Run the model and plot the results, varying the view angle (the other
# option is to vary the solar angle) and plotting the pixel radiance. 
SixSHelpers.Angles.run_and_plot_360(s, 'view', 'pixel_radiance', colorbarlabel=r"At-sensor Spectral Radiance ($W/m^2\!/\mu m$)") 
title('BRDF of Lambertian Surface')



# ....BRDF of Ocean surface
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
# Set solar azimuth and zenith angles and wavelength
s.geometry.solar_a = 0
s.geometry.solar_z = 30
s.wavelength = Wavelength(0.550)
# HomogeneousOcean(wind_speed, wind_azimuth, salinity, pigment_concentration)
s.ground_reflectance = GroundReflectance.HomogeneousOcean(10., 0., -1, 0.) 
# Run the model and plot the results, varying the view angle (the other
# option is to vary the solar angle) and plotting the pixel radiance. 
SixSHelpers.Angles.run_and_plot_360(s, 'view', 'pixel_radiance', colorbarlabel=r"At-sensor Spectral Radiance ($W/m^2\!/\mu m$)") 
title('BRDF of Ocean Surface')



# .... Differet Standard Atmospheres
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.Tropical)
wv , trp = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)
wv , mls = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeWinter)
wv , mlw = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.SubarcticSummer)
wv , sas = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.SubarcticWinter)
wv , saw = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
figure()
plot(wv, trp, wv, mls, wv, mlw, wv, sas, wv, saw)
xlabel('Wavelength (um)')
ylabel('Spectral Radiance [W m-2 um-1]')
title('Radiance from Different Standard Atmospheres')
legend(['Tropical', 'Midlatitude Summer', 'Midlatitude Winter', 'Subarctic Summer', 'Subarctic Winter'], loc='best')


# .... Different AOTs
from Py6S import *
s = SixS()
s.sixs_path = '/Users/vonw/radtran/6SV1.1/sixsV1.1'
s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.Tropical)
s.aot550 = 0.0
wv , aot0_00 = SixSHelpers.Wavelengths.run_modis(s, output_name="pixel_radiance")
s.aot550 = 0.25
wv , aot0_25 = SixSHelpers.Wavelengths.run_modis(s, output_name="pixel_radiance")
s.aot550 = 0.50
wv , aot0_50 = SixSHelpers.Wavelengths.run_modis(s, output_name="pixel_radiance")
s.aot550 = 0.75
wv , aot0_75 = SixSHelpers.Wavelengths.run_modis(s, output_name="pixel_radiance")
s.aot550 = 1.0
wv , aot1_00 = SixSHelpers.Wavelengths.run_modis(s, output_name="pixel_radiance")
figure()
plot(wv, aot0_00, '.', wv, aot0_25, '.', wv, aot0_50,'.', wv, aot0_75,'.', wv, aot1_00, '.')
xlabel('Wavelength (um)')
ylabel('Spectral Radiance [W m-2 um-1]')
title('Radiance from Different Aerosol Optical Thicknesses')
legend(['0.00', '0.25', '0.50', '0.75', '1.00'], loc='best')
