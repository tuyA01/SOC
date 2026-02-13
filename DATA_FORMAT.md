# Data Format and Requirements

## Satellite Imagery
- **Resolution**: Minimum of 30m resolution is preferred.
- **Format**: GeoTIFF (.tif) is the preferable format.
- **Bands**: Must include at least RGB and NIR bands.

## Climate Data
- **Parameters**: Temperature, Precipitation, Humidity.
- **Format**: NetCDF or CSV formats are acceptable.
- **Time Frame**: Data must cover the same time span as the project duration, with daily values preferred.

## Digital Elevation Model (DEM)
- **Resolution**: A minimum resolution of 10m is required.
- **Format**: GeoTIFF (.tif) preferred.
- **Projection**: All data must be in the same coordinate reference system (CRS).

## Soil Data
- **Properties**: pH, Organic Matter, Texture.
- **Format**: Shapefile (.shp) or CSV formats.
- **Sampling Depth**: Specify sampling depths in cm (0-5cm, 5-15cm, 15-30cm).