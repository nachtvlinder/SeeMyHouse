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
import PySimpleGUI as sg


# Global variables
path = f""

# GUI stuff
sg.theme("SolarizedDark")
layout = [[sg.Text("Welcome to See My House!")],
          [sg.Text("Choose a GeoTIFF file: "), sg.Input(),
           sg.FileBrowse(key="-IN-")],
          [sg.Button("OK")]]

window = sg.Window("See My House",
                   layout
                   )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "OK":
        path = values["-IN-"]

window.close()


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


# A filepath needs to be provided
# The user can then input a set
# of coordinates provided in WGS84,
# the generally known standard coordinate system

# Welcome statement
print("Welcome to SeeMyHouse")

# Compatibility checks
tiff_available = input("Can you provide your own GeoTIFF file for 3D plotting? (y/n) ")
tiff_crs_compatible = input("Please not that only files"
                            " using Belgian Lambert crs are \n"
                            "compatible. That includes the files \n"
                            "you can download on the geopunt.be website, \n"
                            "given you use the .tif file found in the \n"
                            "\"GeoTIFF\" folder of the zip-file.\n"
                            "Is your file compatible? (y/n) ")

if tiff_available == ("y" or "Y") and tiff_crs_compatible == ("y" or "Y"):
    path = input("Please provide the filepath of your GeoTIFF: ")
    print(f"Your filepath: {path}")
else:
    print("I'm afraid I can't help you yet.")
    quit()

# Reading the file into a rasterio object
print("Examining file")
image = rasterio.open(path)
print("File received")

# Coordinate input by user
print("At what coordinates do you want me to look?")
print("Please provide latitude and longitude \n"
      "in the following format: degrees minutes seconds \n"
      "(separated by spaces, no unit symbols or names)")
latitude = input("Latitude: ")
longitude = input("Longitude: ")
name = input("Give your plot a name: ")

# Conversion to floats
latitude = coordinate_to_float(latitude)
longitude = coordinate_to_float(longitude)

# Convert from WGS84 to Belgian Lambert
converter = pyproj.Transformer.from_crs('epsg:4326', 'epsg:31370')
x, y = converter.transform(latitude, longitude)

# Construct window
# Define borders of window
window_margin = int(input("To zoom in to your house, we would like you \n"
                          "to estimate how wide or deep it is in metres. \n"
                          "Use whichever value is the largest, so your whole \n"
                          "house can fit on the 3D model: ")) / 2 + 10
left = x - window_margin
right = x + window_margin
bottom = y - window_margin
top = y + window_margin

# Create window object
area_of_interest = image.read(1, window=rw.from_bounds(
    left, bottom, right, top,
    image.transform))

# Convert to pandas dataframe
heightmap = pd.DataFrame(data=area_of_interest)

# Creating the plotly figure (3D model)
fig = go.Figure(data=[go.Surface(z=heightmap.values,
                                 colorscale="Picnic")])

# Set name and properties for good visual
# The 'aspectmode' in the scene argument makes
# sure the model scales correctly and realistically,
# while 'autosize' is needed to make the plot large enough
# and responsive to browser window size
fig.update_layout(title=name, autosize=True,
                  scene=dict(aspectmode="data",
                             xaxis_autorange="reversed"),
                  )

# Ready prompt
print(f"3D plot ready. Saved as {name}.html.")

# This will save the plot
# to an interactive html file
# and open it in the standard browser
fig.write_html(f'{name}.html', auto_open=True)

# Always exit with a smile
print("Thank you for using SeeMyHouse!")
