# placeholder

import plotly.graph_objects as go
import pandas as pd
import rasterio
import pyproj

# Global variables
path = f""

# This will import the given file
# A filepath needs to be provided
# The user can then input a set
# of coordinates provided in WGS84,
# the generally known standard coordinate system
print("Welcome to SeeMyHouse")
tiff_available = input("Can you provide your own GeoTIFF file for 3D plotting? (y/n) ")
tiff_crs_compatible = input("Please not that only files"
                            " using Belgian Lambert crs are "
                            "compatible. Is your file compatible? (y/n) ")
if tiff_available==("y" or "Y") and tiff_crs_compatible==("y" or "Y"):
    path = input("Please provide the filepath of your GeoTIFF: ")
    print(f"Your filepath: {path}")
else:
    print("I'm afraid I can't help you yet.")
    quit()

print("Examining file")
# Here comes the read statement,
# followed by confirmation and a request
# for coordinates to plot
image = rasterio.open(path)
print("File received")
print("At what coordinates do you want me to plot?")
latitude = float(input("Latitude: "))
longitude = float(input("Longitude: "))
# which we then need to convert from WGS84 to Belgian Lambert
# returning them for confirmation
converter = pyproj.Transformer.from_crs('epsg:4326', 'epsg:31370')
x, y = converter.transform(latitude, longitude)

# and use them to read a window around the coordinates

# creating a bouding box around the coordinate point
left = x - 100
right = x + 100
bottom = y - 100
top = y + 100

# followed by converting the resulting window,
# which is returned by rasterio as an nd-array,
# into a pandas dataframe
area_of_interest = image.read(1, window=from_bounds(left, bottom, right, top, image.transform))

# We then use plotly to render a 3D plot
# of this dataframe, based on its x, y and z data.
#codecomeshere

# The following code is part of the first trial plot
# in the next steps, and will be tweaked to read in the
# converted numpy nd-array
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

# The following code already creates a trial plot
# in an automatically opened html file,
# and will be used to plot the data from the
# dataframe generated in the previous step
fig = go.Figure(data=[go.Surface(z=z_data.values)])

# The figure created in the previous step can be tweaked
# on its appearance/layout here. For personal note, the
# only thing I intend to change here is the colorscale.
# Todo: find a way to select a better colorscale
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90),
                 colorscale=go.layout.Colorscale(diverging='greens'))

# This will save the plot
# to an interactive html file
# and open it in the standard browser
fig.write_html('HTML_plots/script_figure.html', auto_open=True)
