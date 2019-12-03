# Derived from Lesson 5 -  Work with Landsat Remote Sensing Data in Python
# ....https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-in-python/landsat-bands-geotif-in-Python/
import os
import numpy as np
# File manipulation
from glob import glob
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio as rio
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# Plot LANDSAT BAND 4
all_landsat_post_bands = glob('/Users/vonw/data/landsat/coldspringsfire/landsat_collect/LC080340322016070701T1-SC20180214145604/crop/*band*.tif')
all_landsat_post_bands.sort()
with rio.open(all_landsat_post_bands[3]) as src:
    landsat_band4 = src.read()
ep.plot_bands(landsat_band4[0],
              title="Landsat Cropped Band 4\nColdsprings Fire Scar",
              scale=False)
plt.show()

# Plot LANDSAT AEROSOLs
all_landsat_post_bands = glob('/Users/vonw/data/landsat/coldspringsfire/landsat_collect/LC080340322016070701T1-SC20180214145604/crop/*aerosol*.tif')
all_landsat_post_bands.sort()
src = rio.open(all_landsat_post_bands[0])
landsat_aerosol = src.read()
ep.plot_bands(landsat_aerosol,
              title="Landsat Aerosol Band",
              scale=False)
plt.show()
