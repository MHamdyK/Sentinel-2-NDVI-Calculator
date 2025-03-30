# Sentinel-2-NDVI-Calculator
A simple Python project that computes NDVI from Sentinel‑2 imagery. It reads red and NIR bands, applies scaling, calculates NDVI, exports a GeoTIFF, and visualizes the results using matplotlib.

#Overview
This project is designed to calculate the Normalized Difference Vegetation Index (NDVI), which is a key indicator of vegetation health. The script:

-Reads Sentinel-2 red (B04) and near-infrared (B08) band images.

-Applies a scaling factor to convert digital numbers to reflectance, I used a scaling factor of dividing by 1000 as mentioned in this thread: https://gis.stackexchange.com/questions/173145/radiometric-calibration-of-sentinel-2-products

-Computes NDVI using the formula:
NDVI = (NIR - Red) / (NIR + Red)

-Exports the resulting NDVI map as a GeoTIFF, exported GeoTIFF is provided in the processed folder inside a .zip file since it is greater than 100MB.

-Visualizes the NDVI using matplotlib.

# Directory Structure
```
Sentinel-2-NDVI-Calculator/
├── data/
│   ├── raw/                   # Input images (red and NIR bands)
│   │   ├── red_band.jp2
│   │   └── nir_band.jp2
│   └── processed/             # Output NDVI image
│       └── ndvi.tif
├── notebooks/                 # (Optional) Jupyter notebooks for exploratory analysis
│   └── analysis.ipynb
├── src/                       # Source code
│   └── ndvi_calculation.py
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```
# Installation
1- Clone the Repo 
```
git clone https://github.com/MHamdyK/Sentinel-2-NDVI-Calculator.git
cd Sentinel-2-NDVI-Calculator
```
2- Create and Activate a Virtual Environment: (This is optional ofc, but recommended)
```
python3 -m venv venv
source venv/bin/activate
```
3- Install Dependencies:
```
pip install -r requirements.txt
```
or you could do pip install for the 3 libraries mentioned in the requirements.txt (rasterio,numpy and matplotlib) file could use the versions mentioned or newer.

# Usage
1. Prepare the Data:
put the sentinel-2 band images (red and NIR) provided in the `data/raw/` folder.
2. Run the NDVI Calculation Script:
```
python src/ndvi_calculation.py
```
