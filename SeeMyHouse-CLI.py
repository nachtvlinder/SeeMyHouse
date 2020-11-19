# SeeMyHouse script app
# 1: import statements
# 1.5: global variables
# 2: locally defined functions
# 3: program implementation

import plotly.graph_objects as go
import pandas as pd
import rasterio
import rasterio.windows as rw
import pyproj

# Global variables
path = f""


# Self-defined functions
# Convert degrees, minutes, seconds format coordinates to float
def coordinate_to_float(dms_string):
    # split input string
    dms_list = dms_string.split(" ")
    # assign elements
    degrees = float(dms_list[0])
    minutes = float(dms_list[1])
    seconds = float(dms_list[2])
    # conversion calculation
    float_coordinate = degrees + (minutes / 60) + (seconds / 3600)
    return float_coordinate


# This will import the given file
# A filepath needs to be provided
# The user can then input a set
# of coordinates provided in WGS84,
# the generally known standard coordinate system
print("Welcome to SeeMyHouse")
tiff_available = "y"  # test-value # input("Can you provide your own GeoTIFF file for 3D plotting? (y/n) ")
tiff_crs_compatible = "y"  # test-value # input("Please not that only files"
# " using Belgian Lambert crs are "
# "compatible. That includes the files "
# "you can download on the geopunt.be website, "
# "given you use the .tif file found in the "
# "\"GeoTIFF\" folder of the zip-file."
# "Is your file compatible? (y/n) ")
if tiff_available == ("y" or "Y") and tiff_crs_compatible == ("y" or "Y"):
    path = "coredata/DHMVIIDSMRAS1m_k13/GeoTIFF/DHMVIIDSMRAS1m_k13.tif"
    # test-value #input("Please provide the filepath of your GeoTIFF: ")
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
print("Please provide latitude and longitude \n"
      "in the following format: degrees minutes seconds \n"
      "(separated by spaces)")
latitude = "51 12 31.7"  # test-value # input("Latitude: ")
longitude = "3 13 27.5"  # test-value # input("Longitude: ")
name = input("Give your plot a name: ")

# Conversion to floats
latitude = coordinate_to_float(latitude)
longitude = coordinate_to_float(longitude)

# which we then need to convert from WGS84 to Belgian Lambert
# returning them for confirmation
converter = pyproj.Transformer.from_crs('epsg:4326', 'epsg:31370')
x, y = converter.transform(latitude, longitude)

# and use them to read a window around the coordinates
window_margin = 100
# creating a bounding box around the coordinate point
left = x - window_margin
right = x + window_margin
bottom = y - window_margin
top = y + window_margin

# followed by converting the resulting window,
# which is returned by rasterio as an nd-array,
# into a pandas dataframe
area_of_interest = image.read(1, window=rw.from_bounds(
    left, bottom, right, top,
    image.transform))

height_values = pd.DataFrame(data=area_of_interest)

# The following code creates a plot
# in an automatically opened html file,
# and will be used to plot the data from the
# dataframe generated in the previous step
fig = go.Figure(data=[go.Surface(z=height_values.values,
                                 colorscale="Portland")])

# The figure created in the previous step can be tweaked
# on its appearance/layout here. For personal note, the
# only thing I intend to change here is the color scale.
# Todo: find a way to get a better color, scale and sizing
fig.update_layout(title=name, autosize=False,
                  # width=750, height=750,
                  scene=dict(aspectmode="manual",
                            aspectratio=dict(x=10, y=10, z=0.2)
                            ),
                  # margin=dict(l=65, r=50, b=65, t=90),
                  # colorscale=go.layout.Colorscale(diverging='greens')
                  )

# Let's prompt the user when ready, since
# the plotting may take some time and we
# don't want to bluntly pop up a browser window
# amidst the sought-out distractions of their waiting time
print("3D plot ready.")
# prompt_to_open = input("Do you want to only save the file, or open it immediately in "
#                        "your browser? (for save type \"s\", for open type \"o\", "
#                        "followed by enter) ")

# This will save the plot
# to an interactive html file
# and open it in the standard browser
fig.write_html(f'testplots/{name}.html', auto_open=True)

# Always exit with a smile
print("Thank you for using SeeMyHouse!")
