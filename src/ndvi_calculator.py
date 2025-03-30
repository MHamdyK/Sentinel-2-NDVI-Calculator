import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# File paths to the red and NIR bands B4 is the RED band and b8 is NIR band
red_path = '/media/mohamdy/HDD 1/Alaska/SENTINEL-2 DATASET/TEST_DATASET/S2C_MSIL1C_20250131T204731_N0511_R014_T07VEL_20250131T221753.SAFE/GRANULE/L1C_T07VEL_A002129_20250131T204744/IMG_DATA/T07VEL_20250131T204731_B04.jp2'
nir_path = '/media/mohamdy/HDD 1/Alaska/SENTINEL-2 DATASET/TEST_DATASET/S2C_MSIL1C_20250131T204731_N0511_R014_T07VEL_20250131T221753.SAFE/GRANULE/L1C_T07VEL_A002129_20250131T204744/IMG_DATA/T07VEL_20250131T204731_B08.jp2'

# Open the red band and read the data.
with rasterio.open(red_path) as red_ds:
    # reading as float for NDVI calculations 
    red = red_ds.read(1).astype('float64')
    profile = red_ds.profile  # Save metadata for later use. we will use it later when writing the output, it saves things like (width,height, CRS, etc...)

# Open the NIR band and read the data.
with rasterio.open(nir_path) as nir_ds:
    nir = nir_ds.read(1).astype('float64')

# Applying the Sentinel-2 scaling factor (typically 0.0001) to convert digital numbers to reflectance. found this information on https://gis.stackexchange.com/questions/173145/radiometric-calibration-of-sentinel-2-products
scale_factor = 0.0001
red_scaled = red * scale_factor
nir_scaled = nir * scale_factor

# Calculate NDVI: (NIR - Red) / (NIR + Red)
ndvi =  (nir_scaled - red_scaled) / (nir_scaled + red_scaled)

# Print NDVI statistics
print("NDVI stats: min={:.3f}, max={:.3f}, mean={:.3f}".format(
    np.nanmin(ndvi), np.nanmax(ndvi), np.nanmean(ndvi)
))

output_dir = '/media/mohamdy/HDD 1/Alaska/SENTINEL-2 DATASET/Output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, 'ndvi.tif')

# Updating metadata
ndvi_profile = profile.copy()
#force output to GeoTIFF (GTiff) and set data type to float32.
ndvi_profile.update(driver='GTiff', dtype=rasterio.float32, count=1)

# Write the NDVI array to a new GeoTIFF file.
with rasterio.open(output_path, 'w', **ndvi_profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

# Plot the NDVI image.
plt.figure(figsize=(10, 8))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI from Sentinel-2')
plt.xlabel('Column #')
plt.ylabel('Row #')
plt.show()